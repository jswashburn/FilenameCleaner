from unittest import TestCase
from formatting import Formatter
from styling import stylers

class TestFormatter(TestCase):
    
    def setUp(self):
        self.pascal_formatter = Formatter(stylers["pascal"])
        self.camel_formatter = Formatter(stylers["camel"])
    
    def test_formats_filename_pascal(self):
        unformatted = "this_file needs_Some_Formatting.exe"
        expected = "ThisFileNeedsSomeFormatting.exe"
        actual = self.pascal_formatter.format(unformatted)
        self.assertEqual(actual, expected)
    
    def test_formats_filename_camel(self):
        unformatted = "Pascal_Case Sure Is the-Bomb.cs.html"
        expected = "pascalCaseSureIsTheBomb.cs.html"
        actual = self.camel_formatter.format(unformatted)
        self.assertEqual(actual, expected)
    
    def test_removes_separators(self):
        unformatted = "please_remove all-these_separators"
        expected = "please remove all these separators"
        actual = self.pascal_formatter.remove_separators(unformatted)
        self.assertEqual(actual, expected)
    
    def test_splits_path(self):
        unformatted = "some_file.cs.html"
        expected = ("some_file", ".cs.html")
        actual = self.pascal_formatter.split_path(unformatted)
        self.assertEqual(actual, expected)