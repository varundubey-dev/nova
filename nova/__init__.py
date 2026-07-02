from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("nova-pl")
except PackageNotFoundError:
    __version__ = "1.1.0"