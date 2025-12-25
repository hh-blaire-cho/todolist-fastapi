# app/main.py
import pathlib
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from sqlalchemy import text

from app.core.db import Base, async_session_factory, engine


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    # 서버 시작시 실행. 테이블 drop & create
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # 초기 데이터 insert (async session 사용)
    sql_file = pathlib.Path("app/data.sql")
    if sql_file.exists():
        sql_text = sql_file.read_text(encoding="utf-8")  # 인코딩 안쓰면 pylint 에러

        async with async_session_factory() as session:
            for statement in sql_text.split(";"):
                stmt = statement.strip()
                if stmt:
                    await session.execute(text(stmt))
            await session.commit()

    yield  # startup 과 shutdown을 가르는 경계선
    # (shutdown 시 할 일 있으면 여기에)
    # await engine.dispose()


main_app = FastAPI(lifespan=lifespan)
