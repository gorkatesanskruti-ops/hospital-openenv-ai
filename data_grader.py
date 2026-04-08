def grade_data(output):
    try:
        if len(output) < 3 and all(d["name"] is not None for d in output):
            return 1.0
        return 0.6
    except:
        return 0.0