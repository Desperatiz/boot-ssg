import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_plain(self):
        node = LeafNode(None, "This is a text without a tag")
        self.assertEqual(node.to_html(), "This is a text without a tag")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "This is a heading!")
        self.assertEqual(node.to_html(), "<h1>This is a heading!</h1>")

    def test_leaf_with_props(self):
        node = LeafNode("a", "Link to boot dev", {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev" target="_blank">Link to boot dev</a>')

    def test_leaf_no_value_raises(self):
        node = LeafNode("span", None)
        with self.assertRaises(ValueError):
            node.to_html()



if __name__ == "__main__":
    unittest.main()