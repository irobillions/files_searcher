class BaseError(Exception):
    def __int__(self, message=None):
        if message is None:
            message = self.default_message()
        super().__init__(message)

    def default_message(self):
        return "An error occur during the process"
