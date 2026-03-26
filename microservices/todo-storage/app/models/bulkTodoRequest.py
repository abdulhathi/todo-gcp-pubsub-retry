from typing import List
from app.models.todo import Todo
from pydantic import BaseModel


class BulkTodoRequest(BaseModel):
  todos: List[Todo]
