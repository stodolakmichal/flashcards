import os
from io import StringIO
from unittest.mock import patch
from main import Words
from main import Json_Operations

import pytest


@pytest.fixture
def patched_json():
    patched_json = {"ciao": "czesc"}
    return patched_json


@pytest.fixture
def words_instance(patched_json):
    with patch("main.open", return_value=StringIO()):
        yield Words(patched_json)


@pytest.fixture
def Json_Operations_instance():
    current_directory = os.path.dirname(os.path.dirname(__file__))
    with patch('os.getcwd', return_value=current_directory):
        json_operations = Json_Operations()
    return json_operations
