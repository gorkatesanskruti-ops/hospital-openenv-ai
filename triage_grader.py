def grade_triage(output):
    if "urgent" in output.lower():
        return 1.0
    return 0.2