from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

HEADER_RE = re.compile(r'^(#{1,6})\s+(.+)$')
CODE_BLOCK_RE = re.compile(r'^```[\s\S]*?```$', re.MULTILINE)
QUOTE_BLOCK_RE = re.compile(r'^(?:> .*(?:\n|$))+$', re.MULTILINE)
UNORDERED_LIST_RE = re.compile(r'^(?:- .*(?:\n|$))+$', re.MULTILINE)
ORDERED_LIST_RE = re.compile(r'^(?:[1-9][0-9]*\. .*(?:\n|$))+$', re.MULTILINE)

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]

def block_to_block_type(block):    
    match block:
        case _ if HEADER_RE.fullmatch(block):
            return BlockType.HEADING
        case _ if CODE_BLOCK_RE.fullmatch(block):
            return BlockType.CODE
        case _ if QUOTE_BLOCK_RE.fullmatch(block):
            return BlockType.QUOTE
        case _ if UNORDERED_LIST_RE.fullmatch(block):
            return BlockType.UNORDERED_LIST
        case _ if ORDERED_LIST_RE.fullmatch(block):
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH