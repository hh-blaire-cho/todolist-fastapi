# app/router/todo_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.service.todo_service import TodoService

router = APIRouter()
service = TodoService()


@router.delete("/", status_code=204)
async def delete_all(db: AsyncSession = Depends(get_db)) -> None:
    await service.delete_all(db)
    return


@router.delete("/{todo_id}", status_code=204)
async def delete_by_id(todo_id: int, db: AsyncSession = Depends(get_db)) -> None:
    await service.delete_by_id(db, todo_id)
    return
