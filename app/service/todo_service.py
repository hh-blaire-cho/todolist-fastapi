# app/service/todo_service.py
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.todo_repository import TodoRepository

todo_repo = TodoRepository()


class TodoService:
    async def delete_all(self, db: AsyncSession) -> None:
        await todo_repo.delete_all(db)

    async def delete_by_id(self, db: AsyncSession, todo_id: int) -> None:
        deleted_todo = await todo_repo.delete_by_id(db, todo_id)
        if not deleted_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return
