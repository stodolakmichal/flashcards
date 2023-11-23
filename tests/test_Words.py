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
    expected_output2 = "\x1b[92mPoprawnie!\x1b[0m\n"
    with patch("builtins.input", return_value=f"{patched_json['ciao']}"):
        words_instance.testKnowledge()
    captured_output2 = capsys.readouterr().out
    assert expected_output2 == captured_output2


def test_testKnowledge_WrongAnswerInfoMessage(words_instance, patched_json, capsys):
    expected_output2 = f"\x1b[91mŹle! Poprawnie: ciao - {patched_json['ciao']}\x1b[0m\n\033[92mPoprawnie!\033[0m".strip()
    with patch("builtins.input", side_effect=["wrong_answer", f"{patched_json['ciao']}"]):
        words_instance.testKnowledge()
    captured_output2 = capsys.readouterr().out.strip()
    assert expected_output2 == captured_output2


