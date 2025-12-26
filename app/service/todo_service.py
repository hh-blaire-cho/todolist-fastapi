# app/service/todo_service.py
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.model.todo import Todo
from app.model.todo_dto import TodoCreateRequest, TodoResponse, TodoUpdateRequest
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

    async def create_todo(
        self, db: AsyncSession, req: TodoCreateRequest
    ) -> TodoResponse:
        todo = await todo_repo.save(
            db,
            Todo(
                content=req.title,
                priority=req.order,
                completed=req.completed,
            ),
        )
        return TodoResponse.from_entity(todo)

    async def update_todo(
        self, db: AsyncSession, todo_id: int, req: TodoUpdateRequest
    ) -> TodoResponse:
        todo = await todo_repo.find_by_id(db, todo_id)
        if todo is None:
            raise HTTPException(status_code=404, detail="Entity not found")
        if req.title is not None:
            todo.content = req.title
        if req.completed is not None:
            todo.completed = req.completed
        if req.order is not None:
            todo.priority = req.order
        await todo_repo.save(
            db, todo
        )  # 자바의 JPA랑 달리 영속성이 없어서, 수정 후 명시적으로 저장해줘야 함.
        return TodoResponse.from_entity(todo)

    async def get_todo(self, db: AsyncSession, todo_id: int) -> TodoResponse:
        todo = await todo_repo.find_by_id(db, todo_id)
        if todo is None:
            raise HTTPException(status_code=404, detail="Entity not found")
        return TodoResponse.from_entity(todo)

    async def get_all_todo(self, db: AsyncSession) -> list[TodoResponse]:
        todolist = await todo_repo.find_all(db)
        return [TodoResponse.from_entity(todo) for todo in todolist]
