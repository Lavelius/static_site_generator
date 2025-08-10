from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to convert to HTML.")
        if self.tag is None:
            return self.value
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