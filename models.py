from pydantic import BaseModel
from typing import Any

class Observation(BaseModel):
    task: str
    input_data: Any

class Action(BaseModel):
    action_type: str
    output: Any

class Reward(BaseModel):
    score: float
    message: str