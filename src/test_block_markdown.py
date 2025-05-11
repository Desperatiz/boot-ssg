import unittest

from block_markdown import BlockType, block_to_block_type, markdown_to_blocks

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

        def test_heading(self):
            self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
            self.assertEqual(block_to_block_type("### Subheading 3"), BlockType.HEADING)
            self.assertEqual(block_to_block_type("####### Too many"), BlockType.PARAGRAPH)  # 7 hashes = invalid

        def test_code_block(self):
            code = "```\ndef foo():\n    return 42\n```"
            self.assertEqual(block_to_block_type(code), BlockType.CODE)

        def test_quote_block(self):
            quote = "> This is a quote\n> on multiple lines"
            self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)
            not_quote = "> This is good\nbut this is not"
            self.assertEqual(block_to_block_type(not_quote), BlockType.PARAGRAPH)

        def test_unordered_list(self):
            ul = "- item 1\n- item 2\n- item 3"
            self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)
            broken_ul = "- item 1\nitem 2"
            self.assertEqual(block_to_block_type(broken_ul), BlockType.PARAGRAPH)

        def test_quote_block_strict(self):
            good = "> Hello\n> world"
            bad  = "> Hello\nthis is not a quote"
            self.assertEqual(block_to_block_type(good), BlockType.QUOTE)
            self.assertEqual(block_to_block_type(bad),  BlockType.PARAGRAPH)

        def test_unordered_list_strict(self):
            good = "- item1\n- item2\n- item3"
            bad  = "- item1\nitem2"
            self.assertEqual(block_to_block_type(good), BlockType.UNORDERED_LIST)
            self.assertEqual(block_to_block_type(bad),  BlockType.PARAGRAPH)

        def test_other_blocks_unchanged(self):
            self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
            code = "```\ncode()\n```"
            self.assertEqual(block_to_block_type(code), BlockType.CODE)
            ordered = "1. one\n2. two"
            self.assertEqual(block_to_block_type(ordered), BlockType.ORDERED_LIST)
            self.assertEqual(block_to_block_type("Just text"), BlockType.PARAGRAPH)

        def test_ordered_list(self):
            ol = "1. First\n2. Second\n3. Third"
            self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)
            bad_ol = "1. First\n3. Skips second"
            self.assertEqual(block_to_block_type(bad_ol), BlockType.ORDERED_LIST)  # Format matches, but logic doesn't
            malformed_ol = "One. Wrong\nTwo. Format"
            self.assertEqual(block_to_block_type(malformed_ol), BlockType.PARAGRAPH)

        def test_paragraph(self):
            self.assertEqual(block_to_block_type("This is just a paragraph."), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()