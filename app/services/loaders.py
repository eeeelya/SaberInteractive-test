import logging

from pipenv.vendor.ruamel import yaml

from orm.repository import insert_data, drop_collection

logger = logging.getLogger(__name__)


async def _read_yaml_file(filename: str):
    with open(filename, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)  # TODO


async def load_builds(filename: str = "build/builds.yaml"):
    collection = "builds"

    await drop_collection(collection)

    data = await _read_yaml_file(filename)

    for build in data[collection]:
        await insert_data(build, collection)


async def load_tasks(filename: str = "build/tasks.yaml"):
    collection = "tasks"

    await drop_collection(collection)

    data = await _read_yaml_file(filename)

    document = {}
    for task in data[collection]:
        if task["name"] in document.keys():
            logger.info("The same build name, pls check")
            continue
        logger.info({task["name"]: task["dependencies"]})
        document[task["name"]] = task["dependencies"]

    await insert_data(document, collection)

