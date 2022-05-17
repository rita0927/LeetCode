class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        
        elif len(self.cache) == self.size:
            # OrderedDict popitem: FIFO(last = False), LIFO(last = True)
            self.cache.popitem(last = False)
        self.cache[key] = value 
            
            
        

        
        
        
        
        
        
        
        
        
        
        

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