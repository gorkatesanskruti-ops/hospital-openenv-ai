from env.models import Observation, Reward
from graders.report_grader import grade_report

class ReportTask:
    name = "report_review"

    def get_observation(self):
        return Observation(
            task="report",
            input_data="Patient temprature is 102 and has infecktion"
        )

    def evaluate(self, action):
        score = grade_report(action.output)
        return Reward(score=score, message="Report evaluated")
        