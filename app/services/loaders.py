import logging

from pipenv.vendor.ruamel import yaml

from orm.repository import insert_data, drop_collection
from services.exceptions import NotFoundHTTPException

logger = logging.getLogger(__name__)


async def _read_yaml_file(filename: str) -> None:
    with open(filename, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError:
            error = f"File {filename} not found."

            logger.error(error)
            raise NotFoundHTTPException(error)


async def load_builds(filename: str = "build/builds.yaml") -> None:
    collection = "builds"

    await drop_collection(collection)  # Clear collection before loading new data

    data = await _read_yaml_file(filename)

    for build in data[collection]:
        await insert_data(build, collection)


async def load_tasks(filename: str = "build/tasks.yaml") -> None:
    collection = "tasks"

    await drop_collection(collection)  # Clear collection before loading new data

    data = await _read_yaml_file(filename)

    document = {}
    for task in data[collection]:
        if task["name"] in document.keys():
            logger.info("The same task name already exists, pls check.")
            continue

        document[task["name"]] = task["dependencies"]

    await insert_data(document, collection)

