class InternalServerError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class BadRequestError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)