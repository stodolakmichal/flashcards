from io import StringIO
from unittest.mock import patch
from main import Words

import pytest


@pytest.fixture
def patched_json():
    patched_json = {"ciao": "czesc"}
    return patched_json


@pytest.fixture
def words_instance(patched_json):
    with patch("main.open", return_value=StringIO()) as mock_open:
        yield Words(patched_json)
