"""Round-trips a document through MongoDB. Needs a running server (see README); uses a throwaway database."""

import asyncio
import os

os.environ["MONGODB_DB"] = "banking_case_agent_test"

from src.repository import close, get_client, get_db, ping


async def main():
    await ping()
    try:
        await get_db().smoke.insert_one({"_id": "x", "ok": True})
        assert await get_db().smoke.find_one({"_id": "x"}) == {"_id": "x", "ok": True}
    finally:
        await get_client().drop_database("banking_case_agent_test")
        await close()
    print("ok")


if __name__ == "__main__":
    asyncio.run(main())
