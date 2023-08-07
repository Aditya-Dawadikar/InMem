from database.Trie import Trie
import random
import time

class DocumentStore(Trie):
    def __init__(self):
        super().__init__()
    
    def generate_unique_id(self):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        current_time = int(time.time())
        random_string_1 = ''.join(random.choices(allowed_chars, k=3))
        random_string_2 = ''.join(random.choices(allowed_chars, k=4))

        unique_id = f'{random_string_1}{current_time}{random_string_2}'
        return unique_id
    
    def insert(self, value):
        document_id = self.generate_unique_id()
        
        op_status, value = super().insert(document_id, value)
        
        if op_status == 1:
            return op_status, {"id": document_id, **value}
