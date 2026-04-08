import random
from env.tasks.triage_task import TriageTask
from env.tasks.report_task import ReportTask
from env.tasks.data_task import DataTask

class HospitalEnv:

    def __init__(self):
        self.tasks = [TriageTask(), ReportTask(), DataTask()]
        self.current_task = None
        self.done = False

    def reset(self):
        self.current_task = random.choice(self.tasks)
        self.done = False
        return self.current_task.get_observation()

    def step(self, action):
        reward = self.current_task.evaluate(action)

        # Reward shaping
        if reward.score > 0.9:
            self.done = True
        elif reward.score < 0.3:
            reward.score -= 0.1

        return (
            self.current_task.get_observation(),
            reward,
            self.done,
            {"task": self.current_task.name}
        )

    def state(self):
        return {
            "task": self.current_task.name,
            "done": self.done
        }