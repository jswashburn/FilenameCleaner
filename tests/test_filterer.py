from unittest import TestCase
from filtering import Filterer

class TestFilterer(TestCase):
    
    def setUp(self):
        self.filterer = Filterer()
        self.example_files = [
            "arg_parsing.py", "clean.py", "notes.txt", "todo.txt",
            "wumpus.exe", "do_not_click.exe", "razorpage.cs.html", "appsettings.json",
            "file", "image.jpg"
        ]

    def reset_patterns(self):
        self.filterer.set_match_pattern(None)
        self.filterer.set_ignore_pattern(None)
    
    def test_filters_matching(self):
        self.reset_patterns()
        self.filterer.set_match_pattern(".*\.py$")
        expected = ["arg_parsing.py","clean.py"]
        actual = self.filterer.filter(self.example_files)
        self.assertEqual(actual, expected)

    def test_filters_ignoring(self):
        self.reset_patterns()
        self.filterer.set_ignore_pattern(".*\.exe$")
        expected = [
            "arg_parsing.py", "clean.py", "notes.txt", "todo.txt",
            "razorpage.cs.html", "appsettings.json", "file", "image.jpg"
        ]
        actual = self.filterer.filter(self.example_files)
        self.assertEqual(actual, expected)
    
    def test_filters_both(self):
        self.reset_patterns()
        self.filterer.set_match_pattern(".*\.exe$")
        self.filterer.set_ignore_pattern("^w")
        expected = ["do_not_click.exe"]
        actual = self.filterer.filter(self.example_files)
        self.assertEqual(actual, expected)