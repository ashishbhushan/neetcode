class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.tail = Node(0,0)
        self.head = Node(0,0)
        self.tail.prev = self.head
        self.head.next = self.tail

    def remove(self, node): # remove from list
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node): # insert before tail
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].val = value
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
            if len(self.cache) > self.cap:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]