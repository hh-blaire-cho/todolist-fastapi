# app/repository/todo_repository.py
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.todo import Todo


class TodoRepository:
    async def delete_all(self, db: AsyncSession) -> None:
        # Use a bulk delete statement
        stmt = delete(Todo)
        await db.execute(stmt)
        await db.commit()

    async def delete_by_id(self, db: AsyncSession, todo_id: int) -> bool:
        # Use a instance delete statement
        result = await db.execute(select(Todo).where(Todo.id == todo_id))
        todo = result.scalar_one_or_none()  # returns None if not found
        if todo:
            await db.delete(todo)  # delete the instance
            await db.commit()
            return True  # 삭제 성공
        return False  # 삭제할 대상 없음
