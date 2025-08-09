from textnode import TextNode, TextType

def main():
    new_node = TextNode("This is some text", TextType.BOLD, "http://example.com")
    print(new_node)

main()