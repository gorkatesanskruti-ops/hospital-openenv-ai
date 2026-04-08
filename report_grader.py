def grade_report(output):
    text = output.lower()
    score = 0.0

    if "temperature" in text:
        score += 0.5
    if "infection" in text:
        score += 0.5

    return score