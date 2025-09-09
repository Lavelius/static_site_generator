from enum import Enum

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unorder_list = "unordered_list"
    ordered_list = "ordered_list"

class Block:
    def markdown_to_blocks(text):
        blocks = []
        text_parts = text.split('\n\n')
        for part in text_parts:
            if part.strip():
                blocks.append(part.strip())
        return blocks
    
    def block_to_block_type(text):
        if text.startswith('#'):
            return BlockType.heading
        elif text.startswith('>'):
            return BlockType.quote
        elif text.startswith('```'):
            return BlockType.code
        elif text.startswith('- ') or text.startswith('* '):
            return BlockType.unorder_list
        elif text[0].isdigit() and text[1] == '.':
            return BlockType.ordered_list
        else:
            return BlockType.paragraph
    

    