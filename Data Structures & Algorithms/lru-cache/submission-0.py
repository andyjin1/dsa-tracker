class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None 
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.kv = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right 
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.kv:
            node = self.kv[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else: 
            return -1
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node
    
    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            node = self.kv[key]
            node.val = value 
            self.remove(node)
            self.insert(node)
        
        else:
            node = Node(key, value)
            self.kv[key] = node
            self.insert(node)
        
        if len(self.kv) > self.cap:
            to_remove = self.left.next 
            self.remove(to_remove)
            del self.kv[to_remove.key]
        