import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        node2 = HTMLNode("div", "This is a div", [], {"class": "container"})
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        node2 = HTMLNode("span", "This is a span", [], {"class": "container"})
        self.assertNotEqual(node, node2)
    def test_repr(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        expected_repr = "HTMLNode(tag=div, value=This is a div, children=[], props={'class': 'container'})"
        self.assertEqual(repr(node), expected_repr)
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container", "id": "main"})
        expected_props = 'class="container" id="main"'
        self.assertEqual(node.props_to_html(), expected_props)


if __name__ == "__main__":
    unittest.main()
