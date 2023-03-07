from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Input(BaseModel):
    text: str
    created_at: datetime = datetime.now()


class Response(BaseModel):
    input_text: str
    generated_text: str
    created_at: datetime = datetime.now()


class User(BaseModel):
    inputs: Optional[list[Input]] = []
    responses: Optional[list[Response]] = []
