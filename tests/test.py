import asyncpg
from dotenv import dotenv_values

import asyncio


credentials = {
    "user": dotenv_values().get("PG_USERNAME"),
    "password": dotenv_values().get("PG_PASSWORD"),
    "host": dotenv_values().get("PG_HOST"),
    "port": int(dotenv_values().get("PG_PORT")),
    "database": dotenv_values().get("PG_DBNAME"),
}


async def main():
    pool = await asyncpg.create_pool(**credentials)
    # pool = await asyncpg.create_pool(dsn="postgres://anthonyprime202:123456@localhost:5432/test")
    conn = await pool.acquire()
    try:
        await conn.execute("CREATE TABLE IF NOT EXISTS my_test(x VARCHAR(225))")
        print("Connection was successful")
    finally:
        await pool.release(conn)

asyncio.run(main())