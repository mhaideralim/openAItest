from pydantic import BaseModel


class Query(BaseModel):
    input_text: dict
