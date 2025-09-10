import asyncpg
from typing import Optional

class Database:
    def __init__(self, dsn: str):
        self.dsn = dsn
        self.pool: Optional[asyncpg.Pool] = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(dsn=self.dsn, min_size=1, max_size=10)

    async def disconnect(self):
        if self.pool:
            await self.pool.close()

    async def fetch_users(self):
        async with self.pool.acquire() as connection:
            return await connection.fetch("SELECT id, name, email FROM users")


    async def fetch(self, query: str, *args):
        if not self.pool:
            raise RuntimeError("Database connection is not established.")
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def execute(self, query: str, *args):
        if not self.pool:
            raise RuntimeError("Database connection is not established.")
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)
