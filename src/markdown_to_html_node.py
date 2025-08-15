from leafnode import LeafNode
from htmlnode import HTMLNode
from markdown_to_blocks import Block, BlockType
from textnode import TextNode, TextType
from parentnode import ParentNode


def markdown_to_html_node(markdown):
    blocks = Block.markdown_to_blocks(markdown)
    nodes = []

    for block in blocks:
        block_type = Block.block_to_block_type(block)
        
        if block_type == BlockType.paragraph:
            nodes.append(ParentNode(tag='p', children=text_to_html_nodes(block)))
        elif block_type == BlockType.heading:
            level = block.count('#')
            tag = f'h{level}' if 1 <= level <= 6 else 'h1'
            nodes.append(ParentNode(tag=tag, children=text_to_html_nodes(block[level:].strip())))
        elif block_type == BlockType.code:
            code_content = (block.strip('` ')).strip()
            code_content = code_content.split('\n')
            for i in range(len(code_content)):
                code_content[i] = code_content[i].strip()
            code_content = '\n'.join(code_content) + '\n'
            nodes.append(ParentNode(tag='pre', children=[LeafNode('code', code_content)]))
        elif block_type == BlockType.quote:
            quote_content = block.strip('> ')
            nodes.append(ParentNode(tag='blockquote', children=text_to_html_nodes(quote_content)))
        elif block_type == BlockType.unorder_list:
            items = block.split('\n')
            children = [ParentNode(tag='li', children=text_to_html_nodes(item[2:])) for item in items if item.startswith('- ')]
            nodes.append(ParentNode(tag='ul', children=children))
        elif block_type == BlockType.ordered_list:
            items = block.split('\n')
            children = [ParentNode(tag='li', children=text_to_html_nodes(item[item.index('.') + 1:].strip())) for item in items if item[0].isdigit()]
            nodes.append(ParentNode(tag='ol', children=children))
        else:
            nodes.append(ParentNode(tag=None, children=text_to_html_nodes(block)))

    return ParentNode(tag='div',children=nodes) if nodes else HTMLNode()  # Return a ParentNode if there are children, otherwise an empty HTMLNode.



def text_to_html_nodes(text):
    text_nodes = TextNode.text_to_textnodes(text)
    if not text_nodes:
        return []
    return [node.text_node_to_html_node() for node in text_nodes]