# is_a_directory_error.py
from .error_base import BaseError


class IsADirectoryErrors(BaseError):
    """Exception raised when a directory is found instead of a file"""

    def __init__(self, path, message=None):
        self.path = path
        if message is None:
            message = f"Expected a file but found a directory: {path}"
        super().__init__(message)
