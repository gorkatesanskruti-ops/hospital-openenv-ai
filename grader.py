from env import HospitalEnv
from tasks import TASKS

def evaluate():
    results = []

    for task in TASKS:
        env = HospitalEnv(task["config"])
        state = env.reset()

        total_reward = 0
        steps = 0
        served = 0

        done = False

        while not done:
            action = 0 if state["beds_available"] > 0 else 1
            state, reward, done, _ = env.step(action)

            total_reward += reward
            steps += 1
            served += 1

        results.append({
            "task": task["name"],
            "reward": total_reward,
            "steps": steps,
            "served": served
        })

    final_score = sum(r["reward"] for r in results)

    return {
        "score": final_score,
        "details": results
    }