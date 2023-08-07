from database.Node import Node
from services.ObjectReference import get_object_address
from services.StringManipulation import is_valid_key

class Trie:
    def __init__(self):
        self.root = Node(
            key="ROOT",
            value="ROOT",
            parent=None
        )
        self.key_list = {}
    
    def insert(self,key_string:str, value):
        if not is_valid_key(key_string):
            return -2, f"""Invalid Input "{key_string}" """

        parent_node = None
        curr_node = self.root
        
        key_length = len(key_string)
        i = 0
        
        while i < key_length:
            if curr_node.children.get(key_string[i]) is not None:
                # If Node exists, then traverse ahead
                parent_node = curr_node
                curr_node = curr_node.children[key_string[i]]
            else:
                new_node = Node(
                                    key = key_string[i],
                                    value = None,
                                    parent = curr_node
                                )
                # If Node does not exist, then add new node
                curr_node.children[key_string[i]] = new_node
                parent_node = curr_node
                curr_node = curr_node.children[key_string[i]]
            
            i+=1

        # Add data at the current node
        curr_node.value = value
        # curr_node.describe()
        return 1, value

    def delete_trie_node(self, curr_node):
        if curr_node.key == "ROOT":
            return

        parent = curr_node.parent
        
        if len(parent.children) <= 1 and parent.value is None:
            # current node is the only child
            del curr_node
            self.delete_trie_node(parent)
        else:
            # remove child reference from the parent
            del parent.children[curr_node.key]
            del curr_node

    def delete(self,key_string:str):
        if not is_valid_key(key_string):
            return -2, f"""Invalid Input "{key_string}" """

        parent_node = None
        curr_node = self.root
        
        key_length = len(key_string)
        i = 0
        
        while i < key_length:
            if curr_node.children.get(key_string[i]) is not None:
                # If Node exists, then traverse ahead
                parent_node = curr_node
                curr_node = curr_node.children[key_string[i]]
            else:
                return -1, f"Key {key_string} not found"
            
            i+=1

        # Delete data at the current node
        curr_node.value = None
        
        if len(curr_node.children) == 0:
            # This is a leaf node
            # Traverse Upwards to delete non branching nodes
            self.delete_trie_node(curr_node)
        
        return 1, f"Key {key_string} deleted successfully"
    
    def search(self,key_string:str):
        if not is_valid_key(key_string):
            return -2, f"""Invalid Input "{key_string}" """

        parent_node = None
        curr_node = self.root
        
        key_length = len(key_string)
        i = 0
        
        while i < key_length:
            if curr_node.children.get(key_string[i]) is not None:
                # If Node exists, then traverse ahead
                parent_node = curr_node
                curr_node = curr_node.children[key_string[i]]
            else:
                return -1, f"Key {key_string} not found"
            
            i+=1

        # Return data at the current node
        if curr_node.value is None:
            return -1, f"""key "{key_string}" not found"""

        return 1, curr_node.value
    
    def search_by_prefix(self,key_string:str):
        if not is_valid_key(key_string):
            return -2, f"""Invalid Input "{key_string}" """

        parent_node = None
        curr_node = self.root
        
        key_length = len(key_string)
        i = 0
        
        while i < key_length:
            if curr_node.children.get(key_string[i]) is not None:
                # If Node exists, then traverse ahead
                parent_node = curr_node
                curr_node = curr_node.children[key_string[i]]
            else:
                return -1, f"""Prefix "{key_string}" not found"""
            
            i+=1

        # Start search from current node
        result_list = {}

        if curr_node.value is not None:
            result_list[key_string] = curr_node.value

        for key,value in curr_node.children.items():
            self.list_keys(
                key_string+key,
                value,
                result_list
            )
        return 1, result_list

    def list_keys(self, curr_key_string, curr_node, key_list):
        if curr_node.value is not None:
            # Add Data to final list
            if key_list.get(curr_key_string) is None:
                key_list[curr_key_string] = curr_node.value
        
        # Traverse ahead
        for key,value in curr_node.children.items():
            self.list_keys(
                curr_key_string+key,
                value,
                key_list)

    def describe(self, verbosity):
        curr_node = self.root
        key_list = {}
        
        for key,value in curr_node.children.items():
            self.list_keys(
                key,
                value,
                key_list
            )

        if verbosity:
            for key,value in key_list.items():
                print("----------------------------")
                print(f"key: {key}")
                print(f"value: {value}")
                print("\n")
        
        return 1, key_list
