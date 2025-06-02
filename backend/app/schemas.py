from pydantic import BaseModel, Field, EmailStr
from typing import Any, List, Dict, Optional

class UserRegister(BaseModel):
    user_email: EmailStr = Field(min_length=1, max_length=80)
    user_password: str = Field(min_length=5, max_length=80)
    user_create_at: str

class UserLogin(BaseModel):
    user_email: EmailStr = Field(min_length=1, max_length=80)
    user_password: str = Field(min_length=5, max_length=80)

class Task(BaseModel):
    text_id: int
    date_value: str
    text_value: str

class ColumnType(BaseModel):
    task_id: Optional[int] = None
    task_name: str
    task_value: List[Task]

class UserTask(BaseModel):
    task_data: List[ColumnType]