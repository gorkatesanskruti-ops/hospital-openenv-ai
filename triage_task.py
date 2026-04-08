from env.models import Observation, Reward
from graders.triage_grader import grade_triage

class TriageTask:
    name = "triage"

    def get_observation(self):
        return Observation(
            task="triage",
            input_data="Patient has chest pain and high BP"
        )

    def evaluate(self, action):
        score = grade_triage(action.output)
        return Reward(score=score, message="Triage evaluated")