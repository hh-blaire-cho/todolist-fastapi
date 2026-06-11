# app/core/db.py
from typing import AsyncGenerator

import hvac  # type: ignore[import-untyped]
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.config import get_vault_settings


def _load_database_url() -> str:
    config = get_vault_settings()
    creds = config.get_vault_credentials()
    client = hvac.Client(url=creds["vault_addr"], token=creds["vault_token"])
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
