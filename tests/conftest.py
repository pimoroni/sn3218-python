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
    sys.modules['smbus'] = mock.MagicMock()
    yield sys.modules['smbus']
    del sys.modules['smbus']


@pytest.fixture(scope='function', autouse=False)
def gpio():
    """Mock RPi.GPIO module."""
    GPIO = mock.MagicMock()

    # Fudge for Python < 37 (possibly earlier)
    sys.modules['RPi'] = mock.Mock()
    sys.modules['RPi'].GPIO = GPIO
    sys.modules['RPi.GPIO'] = GPIO
    yield GPIO
    del sys.modules['RPi']
    del sys.modules['RPi.GPIO']
