import subprocess
import sys
from io import StringIO
from unittest.mock import patch

from main import run
import unittest


class testing_main(unittest.TestCase):
    @patch('builtins.input', side_effect=["1", "X"])
    def test_menu_option_1(self, mock_input):
        run()

    @patch('builtins.input', side_effect=["X"])
    def test_menu_option_X(self, mock_input):
        run()

#     def test_menu_output(self):
#         captured_stdout = StringIO()
#         sys.stdout = captured_stdout
#         NotesApp.run(self)
#         sys.stdout = sys.__stdout__
#         captured_stdout = captured_stdout.getvalue()
#
#         assert '''Menu:
# 1. Wyswietl dostepne slowa
# 2. Testuj swoja wiedze
# X. Zamknij program''' in captured_stdout
