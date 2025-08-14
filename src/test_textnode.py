import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code(self):
        node = TextNode("This is code text", TextType.CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code text")
    
    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "http://example.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "http://example.com"})

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "http://example.com/image.jpg")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertIsNone(html_node.value)
        self.assertEqual(html_node.props, {"src": "http://example.com/image.jpg", "alt": "This is an image"})

    def test_invalid_text_type(self):
        node = TextNode("This is invalid", "invalid_type")
        with self.assertRaises(ValueError):
            node.text_node_to_html_node()








    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)
    def test_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIn(node.text_type, TextType)
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        expected_repr = "TextNode(This is a text node, bold, http://example.com)"
        self.assertEqual(repr(node), expected_repr)





    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)


    def test_split_nodes_no_delimiter(self):
        node = TextNode("This is a text node without delimiter", TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is a text node without delimiter")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    def test_split_nodes_multiple_delimiters(self):
        node = TextNode("This is `code` and `another code` block", TextType.TEXT)
        new_nodes = TextNode.split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[3].text, "another code")
        self.assertEqual(new_nodes[4].text, " block")




    def test_extract_markdown_images(self):
        text = "Here is an image ![alt text](http://example.com/image.jpg) and another ![another image](http://example.com/another.jpg)"
        images = TextNode.extract_markdown_images(text)
        self.assertEqual(len(images), 2)
        self.assertEqual(images[0].text, "alt text")
        self.assertEqual(images[0].text_type, TextType.IMAGE)
        self.assertEqual(images[0].url, "http://example.com/image.jpg")
        self.assertEqual(images[1].text, "another image")
        self.assertEqual(images[1].text_type, TextType.IMAGE)
        self.assertEqual(images[1].url, "http://example.com/another.jpg")

    def test_extract_markdown_images_no_images(self):
        text = "This text has no images"
        images = TextNode.extract_markdown_images(text)
        self.assertEqual(images, [])
        self.assertIsInstance(images, list)
        self.assertEqual(len(images), 0)
        self.assertEqual(images, [])
        self.assertIsInstance(images, list)

    def test_extract_markdown_links(self):
        text = "Here is a link [example](http://example.com) and another [another example](http://another.com)"
        links = TextNode.extract_markdown_links(text)
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0].text, "example")
        self.assertEqual(links[0].text_type, TextType.LINK)
        self.assertEqual(links[0].url, "http://example.com")
        self.assertEqual(links[1].text, "another example")
        self.assertEqual(links[1].text_type, TextType.LINK)
        self.assertEqual(links[1].url, "http://another.com")





    def test_split_nodes_image(self):
        node = TextNode("This is text with an image ![alt text](http://example.com/image.jpg) and more text", TextType.TEXT)
        new_nodes = TextNode.split_nodes_image([node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with an image ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "alt text")
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].url, "http://example.com/image.jpg")
        self.assertEqual(new_nodes[2].text, " and more text")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)


    def test_split_nodes_image_no_images(self):
        node = TextNode("This is a text node without images", TextType.TEXT)
        new_nodes = TextNode.split_nodes_image([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is a text node without images")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    def test_split_nodes_image_multiple_images(self):
        node = TextNode("This is text with an image ![first](http://example.com/first.jpg) and another ![second](http://example.com/second.jpg)", TextType.TEXT)
        new_nodes = TextNode.split_nodes_image([node])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "This is text with an image ")
        self.assertEqual(new_nodes[1].text, "first")
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].url, "http://example.com/first.jpg")
        self.assertEqual(new_nodes[2].text, " and another ")
        self.assertEqual(new_nodes[3].text, "second")
        self.assertEqual(new_nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[3].url, "http://example.com/second.jpg")
        


    def test_split_nodes_link(self):
        node = TextNode("This is text with a link [example](http://example.com) and more text", TextType.TEXT)
        new_nodes = TextNode.split_nodes_link([node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a link ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "example")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK)
        self.assertEqual(new_nodes[1].url, "http://example.com")
        self.assertEqual(new_nodes[2].text, " and more text")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_split_nodes_link_no_links(self):
        node = TextNode("This is a text node without links", TextType.TEXT)
        new_nodes = TextNode.split_nodes_link([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is a text node without links")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)


    def test_split_nodes_link_multiple_links(self): 
        node = TextNode("This is text with a link [first](http://example.com/first) and another [second](http://example.com/second)", TextType.TEXT)
        new_nodes = TextNode.split_nodes_link([node])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "This is text with a link ")
        self.assertEqual(new_nodes[1].text, "first")
        self.assertEqual(new_nodes[1].text_type, TextType.LINK)
        self.assertEqual(new_nodes[1].url, "http://example.com/first")
        self.assertEqual(new_nodes[2].text, " and another ")
        self.assertEqual(new_nodes[3].text, "second")
        self.assertEqual(new_nodes[3].text_type, TextType.LINK)
        self.assertEqual(new_nodes[3].url, "http://example.com/second")






    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = TextNode.text_to_textnodes(text)
        self.assertEqual(len(nodes), 10)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "text")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " with an ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[4].text, " word and a ")
        self.assertEqual(nodes[4].text_type, TextType.TEXT) 
        self.assertEqual(nodes[5].text, "code block")
        self.assertEqual(nodes[5].text_type, TextType.CODE)
        self.assertEqual(nodes[6].text, " and an ")
        self.assertEqual(nodes[6].text_type, TextType.TEXT)
        self.assertEqual(nodes[7].text, "obi wan image")
        self.assertEqual(nodes[7].text_type, TextType.IMAGE)
        self.assertEqual(nodes[7].url, "https://i.imgur.com/fJRm4Vk.jpeg")
        self.assertEqual(nodes[8].text, " and a ")
        self.assertEqual(nodes[8].text_type, TextType.TEXT)
        self.assertEqual(nodes[9].text, "link")
        self.assertEqual(nodes[9].text_type, TextType.LINK)
        self.assertEqual(nodes[9].url, "https://boot.dev")

    def test_text_to_textnodes_empty(self):
        text = ""
        nodes = TextNode.text_to_textnodes(text)
        self.assertEqual(nodes, [])

    def test_text_to_textnodes_no_delimiters(self):
        text = "This is a simple text without any special formatting."
        nodes = TextNode.text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "This is a simple text without any special formatting.")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
    


if __name__ == "__main__":
    unittest.main()
