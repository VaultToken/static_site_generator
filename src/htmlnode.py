from enum import Enum

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""

        props_html = ""
        for prop in self.props:
            if props_html == "":
                props_html += f' {prop}="{self.props[prop]}"'
            else:
                props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return (
            f"HtmlNode("
            f"tag={self.tag!r}, "
            f"value={self.value!r}, "
            f"children={self.children!r}, "
            f"props={self.props!r}"
            f")"
        )
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node must have a tag")
        if self.children == None:
            raise ValueError("Parent node must have children")
        
        children_to_html = ""
        for child in self.children:
            children_to_html += child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{children_to_html}</{self.tag}>'