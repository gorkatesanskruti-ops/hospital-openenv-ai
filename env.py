import random

class HospitalEnv:

    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {
            "patients_waiting": random.randint(10, 30),
            "critical_patients": random.randint(2, 8),
            "available_beds": 10,
            "icu_beds": 2,
            "time": 0
        }
        return self.state

    def step(self, action):
        reward = 0

        if action == "ALLOCATE_BED" and self.state["available_beds"] > 0:
            self.state["patients_waiting"] -= 1
            self.state["available_beds"] -= 1
            reward += 10

        elif action == "MOVE_TO_ICU" and self.state["icu_beds"] > 0:
            if self.state["critical_patients"] > 0:
                self.state["critical_patients"] -= 1
                self.state["icu_beds"] -= 1
                reward += 20

        elif action == "WAIT":
            reward -= 5

        self.state["time"] += 1
        return self.state, reward