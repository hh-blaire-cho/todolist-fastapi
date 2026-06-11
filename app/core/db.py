# app/core/db.py
import os
from typing import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")


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
