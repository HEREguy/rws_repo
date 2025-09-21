import unittest
from io import StringIO
import sys
from ..surname import surname

class TestSurname(unittest.TestCase):
    def setUp(self):
        # Capture stdout for testing print statements
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.original_stdout

    def test_surname_output(self):
        """Test that the surname function prints the correct greeting."""
        surname("John")
        self.assertEqual(self.held_output.getvalue(), "Hello, John!\n")

    def test_surname_with_empty_string(self):
        """Test that the surname function works with an empty string."""
        surname("")
        self.assertEqual(self.held_output.getvalue(), "Hello, !\n")


if __name__ == '__main__':
    unittest.main()