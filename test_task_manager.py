
import io
import sys
import unittest
from contextlib import redirect_stdout

from main import show_message, show_collection, tasks


class TestTaskManager(unittest.TestCase):

    def test_show_message_success(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            show_message("Задача добавлена", "success")
        self.assertIn("[Успех] Задача добавлена", buf.getvalue())

    def test_show_message_error(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            show_message("Ошибка ввода", "error")
        self.assertIn("[Ошибка] Ошибка ввода", buf.getvalue())

    def test_show_collection_empty(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            show_collection([])
        self.assertIn("[Инфо] Список задач пуст.", buf.getvalue())

    def test_show_collection_not_empty(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            show_collection(["Задача 1", "Задача 2"])
        output = buf.getvalue()
        self.assertIn("1. Задача 1", output)
        self.assertIn("2. Задача 2", output)


if __name__ == "__main__":
    unittest.main()
