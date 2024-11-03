from pydantic import BaseModel

class Get_Comment(BaseModel):
    ID_reviewer: int
    ID_under_review: int
    review: str