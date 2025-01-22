import asyncio
import glob
import logging

import motor.motor_asyncio
import pytest_asyncio

from app.config.constants import MONGODB_URL

logging.getLogger("faker").setLevel(logging.ERROR)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _as_module(fixture_path: str) -> str:
    return fixture_path.replace("/", ".").replace("\\", ".").replace(".py", "")


pytest_plugins = [
    _as_module(fixture) for fixture in glob.glob("tests/fixtures/[!_]*.py")
]

logging.info("pytest_plugins", pytest_plugins)


@pytest_asyncio.fixture(scope="session")
def event_loop():
    """
    Pytest fixture for setting up a testing event loop
    """
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
    loop.close()
