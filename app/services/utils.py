import logging
import os

from motor.motor_asyncio import AsyncIOMotorClient


def set_logger(filename: str) -> None:
    logger = logging.getLogger()
    file_handler = logging.FileHandler(filename=filename, mode="a")
    formatter = logging.Formatter("[%(asctime)s: %(levelname)s] %(name)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)


async def init_mongo():
    db_name = os.environ.get("MONGO_DB", "default")
    db_url = os.environ.get("MONGO_URL")

    mongo_client = AsyncIOMotorClient(db_url)
    mongo_database = mongo_client[db_name]
    mongo_collections = {
        "builds": mongo_database.get_collection("builds"),
        "tasks": mongo_database.get_collection("tasks"),
    }

    return mongo_client, mongo_database, mongo_collections
