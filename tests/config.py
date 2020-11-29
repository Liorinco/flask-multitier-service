import os


DATABASE_URI = os.environ["DATABASE_URI"]


def configure() -> None:
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    import sys
    sys.path.append(root_dir)
