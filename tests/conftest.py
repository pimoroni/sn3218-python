import sys

import mock
import pytest


@pytest.fixture(scope='function', autouse=False)
def sn3218():
    import sn3218
    yield sn3218
    del sys.modules['sn3218']


@pytest.fixture(scope='function', autouse=False)
def smbus():
    """Mock smbus module."""
    sys.modules['smbus2'] = mock.MagicMock()
    yield sys.modules['smbus2']
    del sys.modules['smbus2']
