# permission_error.py
from .error_base import BaseError


class PermissionErrors(BaseError):
    """Exception raised for permission errors"""
    def __init__(self, filepath, message=None):
        self.filepath = filepath
        if message is None:
            message = f"Permission denied: {filepath}"
        super().__init__(message)
