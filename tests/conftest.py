import pytest
import os
import sys

@pytest.fixture(scope="session", autouse=True)
def setup_env():
    os.environ['LOG_LEVEL'] = 'DEBUG'
