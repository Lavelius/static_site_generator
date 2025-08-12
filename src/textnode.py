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
	
	def split_nodes_delimiter(old_nodes,delimiter,text_type):
		new_nodes = []
		for node in old_nodes:
			if node.text_type != TextType.TEXT:
				new_nodes.append(node)
			else:
				text_parts = node.text.split(delimiter)
				if len(text_parts) == 1:
							print("no delimiter found, returning original node")
							new_nodes.append(node)
				elif len(text_parts)%2 == 0:
					raise ValueError("Closing delimiter not found")
				else:
					print("delimiter found, splitting nodes")
					for i in range(len(text_parts)):
						if text_parts[i] == "":
							continue
						elif i%2 == 0:
							new_nodes.append(TextNode(text_parts[i], node.text_type, node.url))
						else:
							new_nodes.append(TextNode(text_parts[i], text_type, node.url))
		return new_nodes
	
	def extract_markdown_images(text):
		import re
		pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
		matches = re.findall(pattern, text)
		return [TextNode(alt_text, TextType.IMAGE, url) for alt_text, url in matches]
	
	def extract_markdown_links(text):
		import re
		pattern = r'\[([^\]]+)\]\(([^)]+)\)'
		matches = re.findall(pattern, text)
		return [TextNode(link_text, TextType.LINK, url) for link_text, url in matches]
	
	def split_nodes_image(old_nodes):
		new_nodes = []
		for node in old_nodes:
			image_nodes = TextNode.extract_markdown_images(node.text)
			if len(image_nodes) == 0:
				new_nodes.append(node)
			else:
				current_text = node.text
				for image_node in image_nodes:
					working_text = current_text.split(f"![{image_node.text}]({image_node.url})", 1)
					if len(working_text) == 1:
						new_nodes.append(TextNode(working_text[0], TextType.TEXT, node.url))
					else:
						new_nodes.append(TextNode(working_text[0], TextType.TEXT, node.url))
						new_nodes.append(TextNode(image_node.text, TextType.IMAGE, image_node.url))
						current_text = working_text[1]
				if current_text:
					new_nodes.append(TextNode(current_text, TextType.TEXT, node.url))
		return new_nodes

	def split_nodes_link(old_nodes):
		new_nodes = []
		for node in old_nodes:
			link_nodes = TextNode.extract_markdown_links(node.text)
			if len(link_nodes) == 0:
				new_nodes.append(node)
			else:
				current_text = node.text
				for link_node in link_nodes:
					working_text = current_text.split(f"[{link_node.text}]({link_node.url})", 1)
					if len(working_text) == 1:
						new_nodes.append(TextNode(working_text[0], TextType.TEXT, node.url))
					else:
						new_nodes.append(TextNode(working_text[0], TextType.TEXT, node.url))
						new_nodes.append(TextNode(link_node.text, TextType.LINK, link_node.url))
						current_text = working_text[1]
				if current_text:
					new_nodes.append(TextNode(current_text, TextType.TEXT, node.url))
		return new_nodes
	

