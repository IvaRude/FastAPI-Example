import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

DB_URL = f'postgresql+asyncpg://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}'
async_engine = create_async_engine(DB_URL, echo=True)

Base = declarative_base()
async_session = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)


# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


async def init_models():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(init_models())
