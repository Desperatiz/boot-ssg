import os
import shutil

from textnode import TextNode, TextType

def main():
    text_node = TextNode("Test anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)

def copy_content(source, destination):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # /ruta/a/proyecto/src
    public_dir = os.path.join(base_dir, os.pardir, 'public')  # /ruta/a/proyecto/public
    public_dir = os.path.normpath(public_dir)

    if not os.path.exists(destination_path):
        os.mkdir(destination)
    if os.path.exists(destination_path):
        

if __name__ == "__main__":
    main()