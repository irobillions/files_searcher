from src.errors_handling.error_base import BaseError


class FileNotFoundErrors(BaseError):
    def __init__(self,filepath, message):
        self.filepath = filepath

        if message is None:
            message = f"file not found: {self.filepath}"
        super().__init__(message)