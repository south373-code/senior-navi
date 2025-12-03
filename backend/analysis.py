import sqlite3
import pandas as pd
import json
import matplotlib.pyplot as plt
import io
import base64
from database import DB_NAME

def load_data():
    """Load data from the database into a Pandas DataFrame."""
    conn = sqlite3.connect(DB_NAME)
    query = "SELECT * FROM history"
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Convert date column to datetime objects
    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
    return df

def get_analysis_summary():
    """
    Generate a summary of the assessment history.
    Returns a dictionary with:
    - total_assessments
    - average_score
    - level_distribution
    - question_stats (problematic answers count)
    """
    df = load_data()
    
    if df.empty:
        return {
            "total_assessments": 0,
            "average_score": 0,
            "level_distribution": {},
            "question_stats": {}
        }

    # Basic stats
    total = len(df)
    avg_score = df['score'].mean()
    
    # Level distribution
    level_counts = df['level'].value_counts().to_dict()
    
    # Question stats (parsing JSON details)
    # details column contains JSON string of list of answers: [{"question_id": 1, "answer_value": 1}, ...]
    question_stats = {}
    
    for _, row in df.iterrows():
        try:
            details = json.loads(row['details'])
            for answer in details:
                qid = answer.get('question_id')
                val = answer.get('answer_value')
                # Assuming answer_value 1 is "Yes" (problematic/flagged)
                if val == 1:
                    question_stats[qid] = question_stats.get(qid, 0) + 1
        except (json.JSONDecodeError, TypeError):
            continue
            
    return {
        "total_assessments": total,
        "average_score": round(avg_score, 2),
        "level_distribution": level_counts,
        "question_stats": question_stats
    }

def create_score_trend_chart():
    """Generate a line chart of scores over time."""
    df = load_data()
    if df.empty:
        return None

    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['score'], marker='o', linestyle='-')
    plt.title('Assessment Score Trend')
    plt.xlabel('Date')
    plt.ylabel('Score')
    plt.grid(True)
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf

def create_level_dist_chart():
    """Generate a pie chart of care levels."""
    df = load_data()
    if df.empty:
        return None
        
    level_counts = df['level'].value_counts()
    
    plt.figure(figsize=(8, 8))
    plt.pie(level_counts, labels=level_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Care Level Distribution')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf

def create_question_stats_chart():
    """Generate a bar chart of problematic answers per question."""
    summary = get_analysis_summary()
    stats = summary.get('question_stats', {})
    
    if not stats:
        return None
        
    # Sort by question ID
    sorted_stats = dict(sorted(stats.items()))
    
    questions = [f"Q{k}" for k in sorted_stats.keys()]
    counts = list(sorted_stats.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(questions, counts, color='salmon')
    plt.title('Frequency of "Yes" Answers by Question')
    plt.xlabel('Question ID')
    plt.ylabel('Count')
    plt.grid(axis='y')
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf
