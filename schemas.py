from pydantic import BaseModel, Field
from typing import Optional

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt = 0, le = 5)
    complete: Optional[bool] = False

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(min_length=3, default=None)
    description: Optional[str] = Field(min_length=3, max_length=100, default=None)
    priority: Optional[int] = Field(gt = 0, le = 5, default=None)
    complete: Optional[bool] = False

class TodoResponse(TodoRequest):
    class Config:
        from_attributes = True