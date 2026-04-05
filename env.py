import random
from tasks import get_task

class HospitalEnv:

    def __init__(self):
        self.reset()

    def reset(self, level="easy"):
        self.state = get_task(level)
        self.state["time"] = 0
        return self.state

    def step(self, action):
        reward = 0

        # Allocate bed
        if action == "ALLOCATE_BED" and self.state["available_beds"] > 0:
            if self.state["patients_waiting"] > 0:
                self.state["patients_waiting"] -= 1
                self.state["available_beds"] -= 1
                reward += 10

        # Move to ICU
        elif action == "MOVE_TO_ICU" and self.state["icu_beds"] > 0:
            if self.state["critical_patients"] > 0:
                self.state["critical_patients"] -= 1
                self.state["icu_beds"] -= 1
                reward += 25

        # Wait
        elif action == "WAIT":
            reward -= 5

        # Penalty conditions
        if self.state["patients_waiting"] > 20:
            reward -= 10

        if self.state["critical_patients"] > 5:
            reward -= 20

        # Emergency event (innovation 🔥)
        if random.random() < 0.3:
            self.state["patients_waiting"] += random.randint(5, 15)
            self.state["critical_patients"] += random.randint(1, 5)

        # Doctor fatigue (bonus 🔥)
        if self.state["time"] > 10:
            self.state["doctors_available"] = max(1, self.state["doctors_available"] - 1)

        self.state["time"] += 1

        return self.state, reward

    def get_state(self):
        return self.state