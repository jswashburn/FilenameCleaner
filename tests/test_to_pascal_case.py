from unittest import TestCase
from styling import to_pascal_case

class TestToPascalCase(TestCase):
    
    def test_formats_normal(self):
        unformatted = "please make Me pascal Case"
        expected = "PleaseMakeMePascalCase"
        self.assertEqual(to_pascal_case(unformatted), expected)