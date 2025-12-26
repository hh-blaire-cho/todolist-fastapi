# app/model/todo_dto.py
from typing import Optional

from pydantic import BaseModel


class TodoCreateRequest(BaseModel):
    title: str
    order: int = 0
    completed: bool = False


class TodoUpdateRequest(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None
    order: Optional[int] = None


class TodoResponse(BaseModel):
    id: int
    title: str
    order: int
    completed: bool
    url: str

    @classmethod
    def from_entity(cls, todo) -> "TodoResponse":
        return cls(
            id=todo.id,
            title=todo.content,
            order=todo.priority,
            completed=todo.completed,
            url=f"http://localhost:8000/{todo.id}",  # 엔티티 기반 URL 생성
        )
