import logging
import os

from motor.motor_asyncio import AsyncIOMotorClient


def import_settings():
    return {
        "collection": os.environ.get("MONGO_COLLECTION", "default_coll"),
        "db_name": os.environ.get("MONGO_DB", "default"),
        "db_user": os.environ.get("MONGO_USER", "default_user"),
        "db_pass": os.environ.get("MONGO_PASS", "default_pass"),
        "db_url": os.environ.get("MONGO_URL"),
    }


def set_logger(filename: str) -> None:
    logger = logging.getLogger()
    file_handler = logging.FileHandler(filename=filename, mode="a")
    formatter = logging.Formatter("[%(asctime)s: %(levelname)s] %(name)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)


async def init_mongo(db_name: str, db_url: str):
    mongo_client = AsyncIOMotorClient(db_url)
    mongo_database = mongo_client[db_name]
    mongo_collections = {
        "builds": mongo_database.get_collection("builds"),
        "tasks": mongo_database.get_collection("tasks"),
    }

    return mongo_client, mongo_database, mongo_collections
