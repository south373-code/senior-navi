from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import matplotlib.pyplot as plt
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
STATIC_DIR = "static"

# staticディレクトリがなければ作る
os.makedirs(STATIC_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def upload_csv(request: Request, file: UploadFile = File(...)):
    # CSV読み込み
    df = pd.read_csv(file.file)

    # 必要な列があるかチェック
    required_columns = ["年齢", "要介護度", "通院回数", "ADL"]
    for col in required_columns:
        if col not in df.columns:
            df[col] = 0  # なければ0で補う

    # 健康状態スコア計算
    df["健康状態スコア"] = (
        (100 - (df["年齢"] - 65) * 0.5) +
        (100 - df["要介護度"] * 10) +
        (100 - df["通院回数"] * 5) +
        df["ADL"]
    ) / 4

    # グラフ作成
    plt.figure(figsize=(8,5))
    plt.bar(df.index, df["健康状態スコア"], color="skyblue")
    plt.xlabel("利用者")
    plt.ylabel("健康状態スコア")
    plt.title("健康状態スコア一覧")
    plt.tight_layout()
    plot_path = os.path.join(STATIC_DIR, "plot.png")
    plt.savefig(plot_path)
    plt.close()

    # HTMLに渡す
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "tables": [df.to_html(classes='table')],
            "plot_url": f"/static/plot.png"
        }
    )

# staticファイルを配信
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
