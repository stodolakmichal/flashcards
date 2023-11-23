import json

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
    '''Test if file exists'''
    with patch("builtins.open", return_value=FakeFile(patched_json)):
        json_operations = Json_Operations()
    assert json_operations.json_file == patched_json


def test_getParsedDataFromJsonFile_file_not_exist():
    '''Test if function returns {} if file not exist '''
    with patch("builtins.open", side_effect=[FileNotFoundError, FakeFile({})]):
        json_operations = Json_Operations()
    assert json_operations.json_file == {}
