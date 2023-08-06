from services.ObjectReference import get_object_address

class Node:
    def __init__(self, key:str, value=None, parent=None):
        self.key = key
        self.value = value
        self.children = {}
        self.parent = parent
        
        # print(f"Node {key} created")
    
    def get_address(self):
        return get_object_address(self)

    def describe(self):
        print("\n-----------------------------")
        print(f"key: {self.key}")
        print(f"value: {self.value}")
        print(f"parent: {self.parent.key}")
        print(f"children: {self.children}")
        print()
