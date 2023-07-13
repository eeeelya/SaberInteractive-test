import logging

from fastapi import FastAPI

from services.loaders import load_builds, load_tasks
from services.utils import set_logger, init_mongo
from endpoints.routes import router


app = FastAPI(title="Build System")
app.include_router(router, prefix="/api/v1", tags=["tasks-svc"])

logger = logging.getLogger(__name__)


@app.on_event("startup")
async def startup_event():
    set_logger("build_svc.log")

    app.state.mongo_client, app.state.mongo_db, app.state.mongo_collection = await init_mongo()

    await load_builds()
    await load_tasks()

