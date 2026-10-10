"""MongoDB connection. One client per process; MONGODB_URI and MONGODB_DB pick the server and database.

    from src.repository import get_db
    await get_db().cases.insert_one({...})
"""

import os
from functools import cache

from pymongo import AsyncMongoClient


@cache
def get_client():
    return AsyncMongoClient(os.environ.get("MONGODB_URI", "mongodb://localhost:27017"))


def get_db():
    return get_client()[os.environ.get("MONGODB_DB", "banking_case_agent")]


async def ping():
    await get_client().admin.command("ping")


async def close():
    await get_client().close()
    get_client.cache_clear()
