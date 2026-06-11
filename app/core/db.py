# app/core/db.py
import os
from typing import AsyncGenerator

import hvac  # type: ignore[import-untyped]
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


def _load_database_url() -> str:
    vault_addr = os.getenv("VAULT_ADDR", "http://localhost:8200")
    vault_token = os.getenv("VAULT_TOKEN", "dev-token")

    client = hvac.Client(url=vault_addr, token=vault_token)
    secret = client.secrets.kv.v2.read_secret_version(path="todolistapp")
    return secret["data"]["data"]["database_url"]


DATABASE_URL = _load_database_url()


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
