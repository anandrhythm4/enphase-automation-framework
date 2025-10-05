import pytest
from utils.logger import get_logger
from utils.api_helper import load_config

@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture(scope="session")
def logger():
    return get_logger()
