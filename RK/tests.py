from rk1 import *
import unittest
from unittest.mock import patch
from io import StringIO

class TestCDLibraryFunctions(unittest.TestCase):
    def setUp(self):
        self.CD_disks = [
            CD_disk(1, "CD 1", "Фантастика", 100, 1),
            CD_disk(2, "CD 2", "Роман", 150, 1),
            CD_disk(3, "CD 3", "Фэнтези", 200, 2),
        ]
        self.libraries = [
            Library(1, "Библиотека 1"),
            Library(2, "Библиотека 2"),
        ]
        self.CD_disks_libraries = [
            CD_disksLibrary(1, 1),
            CD_disksLibrary(1, 2),
            CD_disksLibrary(2, 2),
            CD_disksLibrary(3, 1),
            CD_disksLibrary(3, 2)
        ]

    @patch('sys.stdout', new_callable=StringIO)
    def test_list_CD_disks_by_library(self, mock_stdout):
        list_CD_disks_by_library(self.CD_disks, self.libraries)
        expected_output = "\nБиблиотека: Библиотека 1\n - CD 1 (Жанр: Фантастика, Цена: 100)\n - CD 2 (Жанр: Роман, Цена: 150)\n" \
                          "Библиотека: Библиотека 2\n - CD 3 (Жанр: Фэнтези, Цена: 200)"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_list_libraries_by_total_CD_disk_price(self, mock_stdout):
        list_libraries_by_total_CD_disk_price(self.CD_disks, self.libraries)
        expected_output = "\nБиблиотека: Библиотека 1, Суммарная цена книг: 250\n" \
                          "Библиотека: Библиотека 2, Суммарная цена книг: 200"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_list_libraries_and_CD_disks_with_keyword(self, mock_stdout):
        keyword = "Библиотека"
        list_libraries_and_CD_disks_with_keyword(self.CD_disks, self.libraries, self.CD_disks_libraries, keyword)
        expected_output = "\nБиблиотека: Библиотека 1\n - CD 1 (Жанр: Фантастика, Цена: 100)\n - CD 3 (Жанр: Фэнтези, Цена: 200)\n" \
                          "Библиотека: Библиотека 2\n - CD 1 (Жанр: Фантастика, Цена: 100)\n - CD 2 (Жанр: Роман, Цена: 150)\n" \
                          " - CD 3 (Жанр: Фэнтези, Цена: 200)"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
