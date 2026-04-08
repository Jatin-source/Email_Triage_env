from pydantic import BaseModel
from typing import List, Optional

class Email(BaseModel):
    id: str
    subject: str
    body: str
    sender: str
    urgency: str
    category: Optional[str] = None


class Observation(BaseModel):
    inbox: List[Email]
    current_email_id: Optional[str]
    last_action: Optional[str]
    step_count: int


class Action(BaseModel):
    action_type: str  # classify, prioritize, reply, archive
    email_id: str
    content: Optional[str] = None


class State(BaseModel):
    inbox: List[Email]
    processed_ids: List[str]
    step_count: int
    score: float