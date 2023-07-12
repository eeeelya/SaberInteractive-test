import logging

from fastapi import APIRouter
from starlette import status

from orm.repository import retrieve_document, retrieve_all_documents
from schemas import BuildName

router = APIRouter()

logger = logging.getLogger("name")


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited


async def get_dict_from_cursor(cursor):
    return await cursor.next()


@router.post("/get_tasks", status_code=status.HTTP_200_OK)
async def get_tasks(name: BuildName):
    build = await retrieve_document({"name": name.name}, "builds")

    tasks_cursor = await retrieve_all_documents("tasks")
    all_tasks = await get_dict_from_cursor(tasks_cursor)

    summary = {}
    for task in build["tasks"]:
        summary[task] = all_tasks[task]

    logger.info(summary)

    return summary
