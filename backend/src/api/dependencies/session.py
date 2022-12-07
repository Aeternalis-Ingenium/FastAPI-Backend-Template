import contextlib
import typing

import fastapi
from sqlalchemy.ext.asyncio import (
    async_sessionmaker as sqlalchemy_async_sessionmaker,
    AsyncSession as SQLAlchemyAsyncSession,
    AsyncSessionTransaction as SQLAlchemyAsyncSessionTransaction,
)

from src.repository.database import async_db


async def get_async_session() -> typing.AsyncGenerator[SQLAlchemyAsyncSession, None]:
    try:
        yield async_db.async_session
    except Exception as e:
        print(e)
        await async_db.async_session.rollback()
    finally:
        await async_db.async_session.close()
