import glob
import logging

logging.getLogger("faker").setLevel(logging.ERROR)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _as_module(fixture_path: str) -> str:
    return fixture_path.replace("/", ".").replace("\\", ".").replace(".py", "")


pytest_plugins = [
    _as_module(fixture) for fixture in glob.glob("tests/fixtures/[!_]*.py")
]

logging.info("pytest_plugins", pytest_plugins)
