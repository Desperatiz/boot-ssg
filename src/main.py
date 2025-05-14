import os
import shutil
import logging

from textnode import TextNode, TextType

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(here, os.pardir))

    static_dir = os.path.join(project_root, 'static')
    public_dir = os.path.join(project_root, 'public')

    copy_to_public(static_dir, public_dir)



def copy_to_public(source, destination, logger=None):
    if logger is None:
        logger = logging.getLogger("sync")
        logger.setLevel(logging.INFO)
        h = logging.StreamHandler()
        h.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        logger.addHandler(h)

    os.makedirs(destination, exist_ok=True)

    for name in os.listdir(destination):
        path = os.path.join(destination, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    for name in os.listdir(source):
        src = os.path.join(source, name)
        dst = os.path.join(destination, name)

        if os.path.isdir(src):
            copy_to_public(src, dst, logger)
        else:
            shutil.copy2(src, dst)

        logger.info(f"Copied: {src} -> {dst}")
        

if __name__ == "__main__":
    main()