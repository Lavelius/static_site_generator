import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a paragraph", {"class": "text"})
        node2 = LeafNode("p", "This is a paragraph", {"class": "text"})
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = LeafNode("p", "This is a paragraph", {"class": "text"})
        node2 = LeafNode("span", "This is a span", {"class": "text"})
        self.assertNotEqual(node, node2)
    def test_repr(self):
        node = LeafNode("p", "This is a paragraph", {"class": "text"})
        expected_repr = "LeafNode(tag=p, value=This is a paragraph, props={'class': 'text'})"
        self.assertEqual(repr(node), expected_repr)
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph", {"class": "text"})
        expected_html = '<p class="text">This is a paragraph</p>'
        self.assertEqual(node.to_html(), expected_html)
    def test_to_html_no_value(self):
        node = LeafNode("p", None, {"class": "text"})
        with self.assertRaises(ValueError):
            node.to_html()
    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a text without a tag", {"class": "text"})
        expected_html = "This is a text without a tag"
        self.assertEqual(node.to_html(), expected_html)
    def test_eq_with_different_attributes(self):
        node = LeafNode("p", "This is a paragraph", {"class": "text"})
        node2 = LeafNode("p", "This is a paragraph", {"id": "unique"})
        self.assertNotEqual(node, node2)
    def test_eq_with_different_values(self):
        node = LeafNode("p", "This is a paragraph", {"class": "text"})
        node2 = LeafNode("p", "This is another paragraph", {"class": "text"})
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
