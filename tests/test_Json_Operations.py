import json

import pytest

from main import Json_Operations
from unittest.mock import patch


class FakeFile:

    def __init__(self, data):
        self.data = data

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def read(self):
        return json.dumps(self.data)

    def write(self, content):
        self.data = json.loads(content)


def test_getParsedDataFromJsonFile_file_exists(patched_json):
    """ Test if file exists """
    with patch("builtins.open", return_value=FakeFile(patched_json)):
        json_operations = Json_Operations()
    assert json_operations.json_file == patched_json


def test_getParsedDataFromJsonFile_file_not_exist():
    """ Test if function returns {} if file not exist """
    with patch("builtins.open", side_effect=[FileNotFoundError, FakeFile({})]):
        json_operations = Json_Operations()
    assert json_operations.json_file == {}


@pytest.mark.parametrize("side_effects",
                         [("1st_word", "1st_translation", "exit"),
                          ("1st_word", "1st_translation", "2nd_word", "2nd_translation", "exit"),
                          ("1st_word", "1st_translation", "2nd_word", "2nd_translation", "3rd_word", "3rd_translation",
                           "exit")])
def test_getWordsToBeAdded(Json_Operations_instance, side_effects):
    with patch('builtins.input', side_effect=side_effects):
        Json_Operations_instance.getWordsToBeAdded()
    for index in range(0, len(side_effects) - 1, 2):
        assert Json_Operations_instance.json_file[side_effects[index]] == side_effects[index + 1]


def test_getWordsToBeAdded_exit(Json_Operations_instance):
    with patch('builtins.input', side_effect=["exit"]):
        Json_Operations_instance.getWordsToBeAdded()


@pytest.mark.parametrize("side_effects", [("1st_word", "2nd_word", "3rd_word")])
def test_getWords(Json_Operations_instance, side_effects):
    returned_words = []
    with patch('builtins.input', side_effect=side_effects):
        for _ in side_effects:
            returned_words.append(Json_Operations_instance.getWords())
    assert returned_words == list(side_effects)

    def test_updateJsonFile():
        # TODO
        pass
