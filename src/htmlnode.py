class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.content = children if children is not None else []
        self.attributes = props if props is not None else {}

    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.content == other.content and
            self.attributes == other.attributes
        )

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return " ".join(f'{key}="{value}"' for key, value in self.attributes.items())
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.content}, props={self.attributes})"