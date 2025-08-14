import unittest

from markdown_to_blocks import Block, BlockType


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = "This is a paragraph.\n\nThis is another paragraph."
        expected_blocks = ["This is a paragraph.", "This is another paragraph."]
        result = Block.markdown_to_blocks(text)
        self.assertEqual(result, expected_blocks)

    def test_markdown_to_blocks_empty(self):
        text = ""
        expected_blocks = []
        result = Block.markdown_to_blocks(text)
        self.assertEqual(result, expected_blocks)

    def test_markdown_to_blocks_single_line(self):
        text = "Single line text."
        expected_blocks = ["Single line text."]
        result = Block.markdown_to_blocks(text)
        self.assertEqual(result, expected_blocks)





    def test_block_to_block_type_paragraph(self):
        text = "This is a paragraph."
        expected_type = Block.block_to_block_type(text)
        self.assertEqual(expected_type, BlockType.paragraph)

    def test_block_to_block_type_heading(self):
        text = "# This is a heading"
        expected_type = Block.block_to_block_type(text)
        self.assertEqual(expected_type, BlockType.heading)

    def test_block_to_block_type_quote(self):
        text = "> This is a quote"
        expected_type = Block.block_to_block_type(text)
        self.assertEqual(expected_type, BlockType.quote)

    def test_block_to_block_type_code(self):
        text = "```python\nprint('Hello, World!')\n```"
        expected_type = Block.block_to_block_type(text)
        self.assertEqual(expected_type, BlockType.code)
    
    def test_block_to_block_type_unordered_list(self):
        text = "- Item 1\n- Item 2"
        expected_type = Block.block_to_block_type(text)
        self.assertEqual(expected_type, BlockType.unorder_list)

    def test_block_to_block_type_ordered_list(self):
        text = "1. First item\n2. Second item"
        expected_type = Block.block_to_block_type(text)
        self.assertEqual(expected_type, BlockType.ordered_list)
    


if __name__ == "__main__":
    unittest.main()