from .models import AssessmentRequest, AssessmentResult

def calculate_score(request: AssessmentRequest) -> AssessmentResult:
    # Simple scoring: Sum of answer values.
    # Assuming questions are phrased such that "Yes" (1) indicates a problem/dependency.
    # Example: "Can you walk alone?" -> No (1) is bad?
    # Wait, requirements say:
    # 1. Walk alone? (Yes=Good, No=Bad)
    # 2. Eat alone? (Yes=Good, No=Bad)
    # 3. Bath alone? (Yes=Good, No=Bad)
    # 4. Toilet alone? (Yes=Good, No=Bad)
    # 5. Memory issues? (Yes=Bad, No=Good)
    
    # We need to standardize. Let's say the frontend sends a "risk score" for each answer.
    # Or we handle it here.
    # Let's assume the frontend sends 1 for "Risk Present" and 0 for "No Risk".
    # So for "Walk alone?", if user says "No", frontend sends 1.
    # For "Memory issues?", if user says "Yes", frontend sends 1.
    
    total_score = sum(a.answer_value for a in request.answers)
    
    if total_score == 0:
        return AssessmentResult(
            score=total_score,
            level="自立",
            message="現在のところ、介護の必要性は低いと考えられます。この調子で健康を維持しましょう。",
            color="green"
        )
    elif total_score <= 2:
        return AssessmentResult(
            score=total_score,
            level="要支援の可能性",
            message="少し生活に不便を感じているかもしれません。地域包括支援センターへの相談をお勧めします。",
            color="yellow"
        )
    else:
        return AssessmentResult(
            score=total_score,
            level="要介護の可能性",
            message="日常生活に支障が出ている可能性があります。早めに医師や専門家に相談してください。",
            color="red"
        )
