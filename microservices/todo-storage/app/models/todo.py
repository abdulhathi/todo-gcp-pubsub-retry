from datetime import datetime
from typing import List
from pydantic import BaseModel

class Todo(BaseModel):
	id: str
	title: str
	status: str
	created_at: datetime