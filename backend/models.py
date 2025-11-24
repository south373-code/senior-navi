from pydantic import BaseModel
from typing import List, Optional

class Answer(BaseModel):
    question_id: int
    answer_value: int  # 0=No (Good), 1=Yes (Bad) or similar scoring

class AssessmentRequest(BaseModel):
    answers: List[Answer]

class AssessmentResult(BaseModel):
    score: int
    level: str
    message: str
    color: str  # "green", "yellow", "red"
