import unittest

import markdown_to_html_node


class Test_Markdown_To_HTML_Node(unittest.TestCase):
    def test_paragraph(self):
        markdown = "This is a paragraph."
        result = markdown_to_html_node.markdown_to_html_node(markdown)
        print(f'Result: {result.to_html()}')
        expected = "<div><p>This is a paragraph.</p></div>"
        self.assertEqual(result.to_html(), expected)

    def test_heading(self):
        markdown = "## This is a heading"
        result = markdown_to_html_node.markdown_to_html_node(markdown)
        print(f'Result: {result.to_html()}')
        expected = "<div><h2>This is a heading</h2></div>"
        self.assertEqual(result.to_html(), expected)

    def test_codeblock(self):
        md = """
            ```
            This is text that _should_ remain
            the **same** even with inline stuff
            ```
            """

        node = markdown_to_html_node.markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        markdown = "> This is a quote."
        result = markdown_to_html_node.markdown_to_html_node(markdown)
        print(f'Result: {result.to_html()}')
        expected = "<div><blockquote>This is a quote.</blockquote></div>"
        self.assertEqual(result.to_html(), expected)

    def test_unordered_list(self):
        markdown = "- Item 1\n- Item 2"
        result = markdown_to_html_node.markdown_to_html_node(markdown)
        print(f'Result: {result.to_html()}')
        expected = "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        self.assertEqual(result.to_html(), expected)

    def test_ordered_list(self):
        markdown = "1. First item\n2. Second item"
        result = markdown_to_html_node.markdown_to_html_node(markdown)
        print(f'Result: {result.to_html()}')
        expected = "<div><ol><li>First item</li><li>Second item</li></ol></div>"
        self.assertEqual(result.to_html(), expected)

    def test_mixed_content(self):
        markdown = "This is a paragraph.\n\n## Heading\n\n- List item 1\n- List item 2"
        result = markdown_to_html_node.markdown_to_html_node(markdown)
        print(f'Result: {result.to_html()}')
        expected = (
            "<div>"
            "<p>This is a paragraph.</p>"
            "<h2>Heading</h2>"
            "<ul><li>List item 1</li><li>List item 2</li></ul>"
            "</div>"
        )
        self.assertEqual(result.to_html(), expected)

    
        


if __name__ == "__main__":
    unittest.main()
