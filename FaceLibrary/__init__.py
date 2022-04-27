from .facelibrary import FaceLibrary
from importlib import metadata

try:
    __version__ = metadata.version("robotframework-facelibrary")
except metadata.PackageNotFoundError:
    pass