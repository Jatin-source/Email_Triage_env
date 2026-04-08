def grade_response(text):
    score = 0.0
    text = text.lower()

    if "sorry" in text:
        score += 0.4
    if "refund" in text:
        score += 0.3
    if len(text) > 20:
        score += 0.3

    return min(score, 1.0)