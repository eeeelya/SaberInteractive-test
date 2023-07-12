from bson import ObjectId
from pymongo.errors import WriteError

import main
from services.exceptions import AlreadyExistsHTTPException


async def retrieve_document(filters, collection: str):
    return await main.app.state.mongo_collection[collection].find_one(filters, {"_id": 0})


async def retrieve_all_documents(collection: str):
    return main.app.state.mongo_collection[collection].find({}, {"_id": 0})


async def drop_collection(collection: str):
    return main.app.state.mongo_collection[collection].drop()


async def insert_data(document: dict, collection: str):
    try:
        await main.app.state.mongo_collection[collection].insert_one(document)
    except WriteError:
        raise AlreadyExistsHTTPException(f"Document with {document} already exists")
