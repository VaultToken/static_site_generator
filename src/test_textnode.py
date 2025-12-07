import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

class Test__text_node_to_html_node(unittest.TestCase):
    def test_single_text_type_node(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        html_node_to_html = html_node.to_html()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node_to_html, "This is a text node")

    def test_single_italic_type_node(self):
        node = TextNode("this is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        html_node_to_html = html_node.to_html()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "this is italic")
        self.assertEqual(html_node_to_html, "<i>this is italic</i>")

    def test_single_link_type_node(self):
        node = TextNode("google", TextType.LINK, "https://www.google.com.au")
        html_node = text_node_to_html_node(node)
        html_node_to_html = html_node.to_html()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "google")
        self.assertEqual(html_node.props, {"href": "https://www.google.com.au"})
        self.assertEqual(html_node_to_html, '<a href="https://www.google.com.au">google</a>')

if __name__ == "__main__":
    unittest.main()