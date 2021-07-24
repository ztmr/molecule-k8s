import pytest


@pytest.fixture
def DRIVER():
    """Return name of the driver to be tested."""
    return "k8s"
