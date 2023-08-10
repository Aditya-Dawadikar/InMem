import json

class DataTypeError(Exception):

    def __init__(self, error_description):
        self.error_description = error_description
    
    def __str__(self):
        return json.dumps(self.error_description)

class CollectiveDataTypeError(Exception):

    def __init__(self,
                 identified_problems: list):
        self.collective_errors = []
        for exception in identified_problems:
            self.collective_errors.append(
                DataTypeError(exception)
            )
    
    def __str__(self):
        error_messages = []
        for error in self.collective_errors:
            error_messages.append(str(error))
        return "\n".join(error_messages)
