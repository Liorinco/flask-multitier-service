import os


SERVICE_HOST = os.environ["SERVICE_HOST"]
SERVICE_PORT = int(os.environ["SERVICE_PORT"])
SERVICE_DEBUG = os.environ["SERVICE_DEBUG"]
DATABASE_URI = os.environ["DATABASE_URI"]


def configure() -> None:
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    import sys
    sys.path.append(root_dir)
