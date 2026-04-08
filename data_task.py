from env.models import Observation, Reward
from graders.data_grader import grade_data

class DataTask:
    name = "data_cleaning"

    def get_observation(self):
        return Observation(
            task="data",
            input_data=[
                {"name": "Saku", "age": 20},
                {"name": "Saku", "age": 20},
                {"name": None, "age": 22}
            ]
        )

    def evaluate(self, action):
        score = grade_data(action.output)
        return Reward(score=score, message="Data evaluated")