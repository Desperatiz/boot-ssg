import unittest

from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_empty_string(self):
            self.assertEqual(markdown_to_blocks(""), [])

        def test_only_whitespace(self):
            self.assertEqual(markdown_to_blocks("   \n\n   "), [])

        def test_no_double_newline(self):
            md = "One line\nSecond line\nThird line"
            self.assertEqual(markdown_to_blocks(md), ["One line\nSecond line\nThird line"])

        def test_multiple_consecutive_blank_lines(self):
            md = "Para1\n\n\n\nPara2"
            self.assertEqual(
                markdown_to_blocks(md),
                ["Para1", "Para2"],
            )

        def test_leading_and_trailing_blank_lines(self):
            md = "\n\nFirst paragraph\n\nSecond paragraph\n\n"
            self.assertEqual(
                markdown_to_blocks(md),
                ["First paragraph", "Second paragraph"],
            )

        def test_single_paragraph(self):
            md = "Just a single paragraph with no breaks."
            self.assertEqual(markdown_to_blocks(md), ["Just a single paragraph with no breaks."])


if __name__ == "__main__":
    unittest.main()