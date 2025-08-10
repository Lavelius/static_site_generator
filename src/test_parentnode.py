import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        parent = ParentNode("p", 
                            [LeafNode("b", "Bold text"),
                             LeafNode(None, "Normal text"),
                             LeafNode("i", "Italic text"),
                             LeafNode(None, "Plain text")])
        expected_html = '<p><b>Bold text</b>Normal text<i>Italic text</i>Plain text</p>'
        self.assertEqual(parent.to_html(), expected_html)
    def test_nested_parent_nodes(self):
        child1 = ParentNode("div", [LeafNode("span", "Child 1")])
        child2 = ParentNode("div", [LeafNode("span", "Child 2")])
        parent = ParentNode("section", [child1, child2])
        expected_html = '<section><div><span>Child 1</span></div><div><span>Child 2</span></div></section>'
        self.assertEqual(parent.to_html(), expected_html)
    def test_empty_children(self):
        parent = ParentNode("div", [])
        expected_html = '<div></div>'
        self.assertEqual(parent.to_html(), expected_html)
    def test_mixed_children(self):
        parent = ParentNode("div", 
                            [LeafNode("span", "Text 1"),
                             LeafNode("span", "Text 2"),
                             ParentNode("p", [LeafNode("b", "Bold text")])])
        expected_html = '<div><span>Text 1</span><span>Text 2</span><p><b>Bold text</b></p></div>'
        self.assertEqual(parent.to_html(), expected_html)
    def test_multiple_levels_of_nesting(self):
        child1 = ParentNode("div", [LeafNode("span", "Child 1")])
        child2 = ParentNode("div", [LeafNode("span", "Child 2")])
        parent = ParentNode("section", [child1, child2, 
                                        ParentNode("article", [LeafNode("p", "Article text")])])
        expected_html = '<section><div><span>Child 1</span></div><div><span>Child 2</span></div><article><p>Article text</p></article></section>'
        self.assertEqual(parent.to_html(), expected_html)
    def test_parentnode_with_props(self):
        parent = ParentNode("div", 
                            [LeafNode("span", "Text")], 
                            {"class": "container", "id": "main"})
        expected_html = '<div class="container" id="main"><span>Text</span></div>'
        self.assertEqual(parent.to_html(), expected_html)
    def test_error_cases(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()


if __name__ == "__main__":
    unittest.main()
