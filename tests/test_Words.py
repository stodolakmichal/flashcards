from unittest.mock import patch

import pytest
from main import Words
from io import StringIO


def test_displayWords(words_instance, capsys):
    words_instance.displayWords()
    expected_output = "ciao - czesc"
    captured_output = capsys.readouterr().out.strip()
    assert expected_output == captured_output


def test_testKnowledge_CorrectAnswerInfoMessage(words_instance, patched_json, capsys):
    expected_output = "Poprawnie!\n"
    with patch("builtins.input", return_value=f"{patched_json['ciao']}"):
        words_instance.testKnowledge()
    captured_output = capsys.readouterr().out
    assert expected_output == captured_output


def test_testKnowledge_WrongAnswerInfoMessage(words_instance, patched_json, capsys):
    expected_output = f"Źle! Poprawnie: ciao - {patched_json['ciao']}\nPoprawnie!".strip()
    with patch("builtins.input", side_effect=["wrong_answer", f"{patched_json['ciao']}"]):
        words_instance.testKnowledge()
    captured_output = capsys.readouterr().out.strip()
    assert expected_output == captured_output


def test_testKnowledge_WrongAnswer10Times(words_instance, capsys):
    expected_output = "Odpowiedziałeś 10 razy źle! Zacznij do nowa!"
    with patch("builtins.input", side_effect=["words_for_test"] * 10):
        words_instance.testKnowledge()
    captured_output = capsys.readouterr().out.strip()
    last_new_line = captured_output.rfind("\n")
    last_print = captured_output[last_new_line + 1:]
    assert expected_output == last_print
