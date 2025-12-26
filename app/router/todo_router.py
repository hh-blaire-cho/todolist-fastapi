# app/router/todo_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.model.todo_dto import TodoCreateRequest, TodoResponse, TodoUpdateRequest
from app.service.todo_service import TodoService

router = APIRouter()
service = TodoService()


@router.delete("/", status_code=204)
async def delete_all(db: AsyncSession = Depends(get_db)) -> None:
    await service.delete_all(db)
    return


@router.get("/", response_model=list[TodoResponse])
async def get_all_todo(db: AsyncSession = Depends(get_db)):
    return await service.get_all_todo(db)


@router.delete("/{todo_id}", status_code=204)
async def delete_by_id(todo_id: int, db: AsyncSession = Depends(get_db)) -> None:
    await service.delete_by_id(db, todo_id)
    return


@router.patch("/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: int,
    req: TodoUpdateRequest,
    db: AsyncSession = Depends(get_db),
):
    return await service.update_todo(db, todo_id, req)


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    return await service.get_todo(db, todo_id)


@router.post("/", response_model=TodoResponse)
async def create_todo(req: TodoCreateRequest, db: AsyncSession = Depends(get_db)):
    return await service.create_todo(db, req)
