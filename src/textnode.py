from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
	TEXT = "text"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text, text_type, URL=None):
		self.text = text
		self.text_type = text_type
		self.url = URL

	def text_node_to_html_node(self):
		if self.text_type == TextType.TEXT:
			return LeafNode(None, self.text)
		elif self.text_type == TextType.BOLD:
			return LeafNode("b", self.text)
		elif self.text_type == TextType.ITALIC:
			return LeafNode("i", self.text)
		elif self.text_type == TextType.CODE:
			return LeafNode("code", self.text)
		elif self.text_type == TextType.LINK and self.url:
			return LeafNode("a", self.text, {"href": self.url})
		elif self.text_type == TextType.IMAGE and self.url:
			return LeafNode("img", None, {"src": self.url, "alt": self.text})
		else:
			raise ValueError(f"Unsupported text type: {self.text_type}")

	# checks if two nodes are equal
	def __eq__(self, other):
		return (
			self.text == other.text and
			self.text_type == other.text_type and
			self.url == other.url
		)

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
	
