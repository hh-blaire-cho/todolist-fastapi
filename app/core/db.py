# app/core/db.py
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/tododb"


class Base(DeclarativeBase):
    pass


engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # spring.jpa.show-sql = true 와 유사
)

async_session_factory = async_sessionmaker(  # pylint: disable=invalid-name
    bind=engine,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator:
    async with async_session_factory() as session:
        yield session
