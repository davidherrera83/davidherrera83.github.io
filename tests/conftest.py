import pytest
from pylenium.driver import Pylenium

@pytest.fixture
def website(py):
    py.visit('https://david-herrera.dev/')
    return py
