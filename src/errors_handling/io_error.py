# io_error.py
from .error_base import BaseError


class IOErrors(BaseError):
    """Exception raised for I/O errors"""

    def __init__(self, message=None):
        if message is None:
            message = "An I/O error occurred"
        super().__init__(message)
