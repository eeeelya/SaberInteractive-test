from pymongo.errors import WriteError

import main
from services.exceptions import AlreadyExistsHTTPException, NotFoundHTTPException


async def retrieve_document(filters, collection: str):
    if document := await main.app.state.mongo_collection[collection].find_one(filters, {"_id": 0}):
        return document
    else:
        raise NotFoundHTTPException(f"Document with specified filters {filters} not found.")


async def retrieve_all_documents(collection: str):
    tasks_cursor = main.app.state.mongo_collection[collection].find({}, {"_id": 0})

    if documents := await tasks_cursor.next():
        return documents
    else:
        raise NotFoundHTTPException(f"Documents in collection {collection} not found.")


async def drop_collection(collection: str):
    return main.app.state.mongo_collection[collection].drop()


async def insert_data(document: dict, collection: str):
    try:
        await main.app.state.mongo_collection[collection].insert_one(document)
    except WriteError:
        raise AlreadyExistsHTTPException(f"Document {document} already exists.")
