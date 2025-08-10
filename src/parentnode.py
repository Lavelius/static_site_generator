from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag to convert to HTML.")
        if self.children is None:
            raise ValueError("ParentNode must have children to convert to HTML.")
        attrs = self.props_to_html()
        children_html = ''.join(child.to_html() for child in self.children)
        if attrs:
            return f"<{self.tag} {attrs}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"