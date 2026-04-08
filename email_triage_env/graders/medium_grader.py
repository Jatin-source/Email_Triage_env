def grade(selected_id, correct_id, action):
    score = 0.0

    if selected_id == correct_id:
        score += 0.5

    if action == "reply":
        score += 0.5

    return score