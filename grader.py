def evaluate(env):

    score = 0

    if env.state["patients_waiting"] < 10:
        score += 50

    if env.state["critical_patients"] == 0:
        score += 100

    if env.state["time"] < 20:
        score += 50

    return score