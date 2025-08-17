import unittest

from extract_title import extract_title


class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is a title\n\nThis is a paragraph."
        result = extract_title(markdown)
        print(f'Result: {result}')
        expected = "This is a title"
        self.assertEqual(result, expected)

    def test_no_title(self):
        markdown = "This is a paragraph without a title."
        result = extract_title(markdown)
        print(f'Result: {result}')
        expected = None
        self.assertIsNone(result)

    def test_multiple_titles(self):
        markdown = "# First Title\n## Second Title\nThis is a paragraph."
        result = extract_title(markdown)
        print(f'Result: {result}')
        expected = "First Title"
        self.assertEqual(result, expected)

    def test_not_h1_heading(self):
        markdown = "## Not a title"
        result = extract_title(markdown)
        print(f'Result: {result}')
        expected = None
        self.assertEqual(result, expected)

    def test_title_at_end(self):
        markdown = "This is a paragraph.\n\n# Title at the end"
        result = extract_title(markdown)
        print(f'Result: {result}')
        expected = "Title at the end"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
