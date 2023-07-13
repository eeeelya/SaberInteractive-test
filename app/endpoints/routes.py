from fastapi import APIRouter
from starlette import status

from orm.repository import retrieve_all_documents, retrieve_document
from models.build import BuildName
from services.orders import create_order_for_task

router = APIRouter()


@router.post("/get_tasks", status_code=status.HTTP_200_OK)
async def get_tasks(name: BuildName):
    build = await retrieve_document({"name": name.name}, "builds")

    all_tasks = await retrieve_all_documents("tasks")

    summary = []
    for task in build["tasks"]:
        order_for_task = create_order_for_task(all_tasks, task)
        summary.extend(order_for_task)

    return summary
