from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            if self.value is None or self.value == "":
                raise ValueError("LeafNode must have a value to convert to HTML.")
            return self.value
        
        # Handle self-closing tags like img
        if self.tag == "img":
            attrs = self.props_to_html()
            return f"<{self.tag} {attrs}>" if attrs else f"<{self.tag}>"
        
        # Handle other tags
        if self.value is None:
            raise ValueError("LeafNode must have a value to convert to HTML.")
        
        attrs = self.props_to_html()
        if attrs:
            return f"<{self.tag} {attrs}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
    def __eq__(self, other):
        return (
            isinstance(other, LeafNode) and
            self.tag == other.tag and
            self.value == other.value and
            self.props == other.props
        )