class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

def insertAfterHead(head, node):
    prev = head.next
    head.next = node
    node.prev = head
    node.next = prev
    prev.prev = node

def delete(node):
    node.prev.next = node.next
    node.next.prev = node.prev

    
class LRUCache:
    def __init__(self, capacity):
        self.map = dict()
        self.capacity = capacity
        self.size = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key, val):
        if key in self.map:
            node = self.map.get(key)
            node.val = val
            delete(node)
            insertAfterHead(self.head, node)
        else:
            node = Node(key, val)
            self.map[key] = node
            if self.capacity == self.size:
                del self.map[self.tail.key]
                delete(self.tail.prev)
                self.size -= 1
            insertAfterHead(self.head, node)

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map.get(key)
        val = node.val
        delete(node)
        insertAfterHead(self.head, node)
        return val

            
cache = LRUCache(4)
cache.put(2, 6)
cache.put(4,7)
cache.put(8,11)
cache.put(7,10)
print(cache.get(2))
print(cache.get(8))
cache.put(5,6)
print(cache.get(7))
cache.put(5,7)
print(cache.get(5))