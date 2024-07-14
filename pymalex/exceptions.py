class PyMalexError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class NoURL(PyMalexError):
    pass


class NoKEY(PyMalexError):
    pass
