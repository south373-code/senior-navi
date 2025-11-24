from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import AssessmentRequest, AssessmentResult
from scoring import calculate_score
from database import init_db, save_result, get_history
import json
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_db()

# Mount static directory if it exists (for production)
if os.path.exists("static"):
    app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")

    @app.get("/")
    async def read_root():
        return FileResponse("static/index.html")

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        # Serve index.html for any path not matched by API
        if full_path.startswith("api"):
            return {"error": "Not Found"}
        return FileResponse("static/index.html")
else:
    @app.get("/")
    def read_root():
        return {"message": "Senior Navi Backend is running (Development Mode)"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/api/assess", response_model=AssessmentResult)
def assess(request: AssessmentRequest):
    result = calculate_score(request)
    # Save to history
    save_result(result.score, result.level, json.dumps([a.dict() for a in request.answers]))
    return result

@app.get("/api/history")
def read_history():
    return get_history()

