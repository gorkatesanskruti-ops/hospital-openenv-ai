import random

class HospitalEnv:
    def __init__(self, config=None):
        config = config or {}
        self.num_beds = config.get("beds", 5)
        self.num_doctors = config.get("doctors", 3)
        self.max_steps = config.get("max_steps", 50)
        self.num_patients = config.get("patients", 10)
        self.reset()

    def reset(self):
        self.step_count = 0
        self.beds_available = self.num_beds
        self.doctors_available = self.num_doctors

        self.patients = []
        for _ in range(self.num_patients):
            self.patients.append(self._generate_patient())

        return self._get_state()

    def _generate_patient(self):
        return {
            "type": random.choice(["normal", "emergency"]),
            "severity": random.randint(1, 5),
            "waiting_time": 0
        }

    def _get_state(self):
        return {
            "patients_waiting": len(self.patients),
            "beds_available": self.beds_available,
            "doctors_available": self.doctors_available
        }

    def step(self, action):
        """
        Action:
        0 -> Treat next patient
        1 -> Skip (wait)
        """
        reward = 0
        done = False
        info = {}

        if not self.patients:
            return self._get_state(), reward, True, info

        # Sort patients: emergency + high severity first
        self.patients.sort(key=lambda x: (x["type"] != "emergency", -x["severity"]))

        patient = self.patients[0]

        if action == 0 and self.beds_available > 0 and self.doctors_available > 0:
            self.patients.pop(0)
            self.beds_available -= 1
            self.doctors_available -= 1

            # Reward Logic (STRONG)
            reward += 30 - patient["waiting_time"]
            reward += patient["severity"] * 6

            if patient["type"] == "emergency":
                reward += 40

        else:
            reward -= 10  # bad action

        # Increase waiting time
        for p in self.patients:
            p["waiting_time"] += 1
            if p["waiting_time"] > 10:
                reward -= 50  # patient leaves

        # Resource penalty
        if self.beds_available > 0:
            reward -= self.beds_available * 2

        # Release resources randomly (simulate discharge)
        self.beds_available = min(self.num_beds, self.beds_available + random.randint(0, 1))
        self.doctors_available = min(self.num_doctors, self.doctors_available + random.randint(0, 1))

        self.step_count += 1
        if self.step_count >= self.max_steps:
            done = True

        return self._get_state(), reward, done, info