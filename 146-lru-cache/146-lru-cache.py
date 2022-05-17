"""
there are pseudo head and pseudo tail to mark the boundary, so that we don't need to check the null node during the update
"""

class DoubleLinkedList():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        self.head.next = self.tail
        self.tail.next = self.head
        
    # add the new node right after head (pseudo)
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next 
        
        self.head.next.prev = node
        self.head.next = node
        
    def _remove_node(self, node):
        prev= node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev
    
    # move the node right after the pseudo head
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
     
    # pop the current last node (right before pseudo tail)
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res 
        

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        
        self._move_to_head(node)
        return node.value

        

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        
        if not node:
            newNode = DoubleLinkedList()
            newNode.key = key
            newNode.value = value
            
            self.cache[key] = newNode
            self.size +=1
            self._add_node(newNode)
            
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)
            

            
            
        

        
        
        
        
        
        
        
        
        
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)





























#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.size = capacity

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.cache.move_to_end(key)
#             return self.cache[key]
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         elif len(self.cache) == self.size:

#             # popitem() returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.
#             self.cache.popitem(last=False)

#         self.cache[key] = value