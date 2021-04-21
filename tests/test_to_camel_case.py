from unittest import TestCase
from styling import to_camel_case

class TestToCamelCase(TestCase):
    
    def test_formats_normal(self):
        unformatted = "I Want To be camel cased"
        expected = "iWantToBeCamelCased"
        self.assertEqual(to_camel_case(unformatted), expected)