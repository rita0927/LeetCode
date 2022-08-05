class ListNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1
        
class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.size = 0
    
    def addNode(self, node):
        node.prev = self.head 
        node.next = self.head.next 
        self.head.next.prev = node
        self.head.next = node
        self.size +=1 
    
    def removeNode(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev
        self.size -= 1
    
    def removeTail(self):
        tail = self.tail.prev
        self.removeNode(tail)
        return tail 
    

    

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.counter = defaultdict(DoubleLinkedList)
        self.min_freq = 0
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.update(key, node.val)
            return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        
        if key in self.cache:
            self.update(key, value)
        else:
            if len(self.cache) == self.capacity:
                lfu_node = self.counter[self.min_freq].removeTail()
                del self.cache[lfu_node.key]
            
            node = ListNode(key, value)
            self.cache[key] = node
            self.min_freq = 1
            self.counter[self.min_freq].addNode(node)
            
    def update(self, key, val):
        node = self.cache[key]
        prev_freq = node.freq
        self.counter[prev_freq].removeNode(node)
        node.val = val
        node.freq += 1
        self.counter[node.freq].addNode(node)
        if prev_freq == self.min_freq and self.counter[self.min_freq].size == 0:
            del self.counter[self.min_freq]
            self.min_freq += 1
        
                
            
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)





# # cache: {key: ListNode}, initialize freq = 1 in the ListNode
# # count: {freq: DoubleLinkedList}, initialize the DLL with the size = 0
# # ListNode with the same freq is added to the DoubleLinkedList
# # DoubleLinkedList maintain the lru becuase the put/get update the freq, and the node is removed/added to different DLL. The front of DLL is always the lru



# class ListNode:
#     def __init__(self, key = 0, val = 0):
#         self.key = key
#         self.val = val
#         self.next = None
#         self.prev = None 
#         self.freq = 1

# class DoubleLinkedList:
#     def __init__(self):
#         self.head = ListNode()
#         self.tail = ListNode()
#         self.head.next = self.tail
#         self.tail.prev = self.head 
#         self.size = 0
        
#     def addNode(self, node):
#         node.prev = self.head 
#         node.next = self.head.next 
#         self.head.next.prev = node
#         self.head.next = node 
#         self.size += 1
        
#     def removeNode(self, node):
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         self.size -= 1
    
#     def removeTail(self):
#         tail = self.tail.prev
#         self.removeNode(tail)
#         return tail 
        


# class LFUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}
#         self.count = defaultdict(DoubleLinkedList)
#         self.min_freq = 0
        

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         else:
#             node = self.cache[key]
#             self.update(key, node.val)
#             return node.val        
        
        
#     def put(self, key: int, value: int) -> None:
#         if self.capacity == 0:
#             return 
        
#         if key in self.cache:

#            # node will be updated, and the cache stores the reference (updated automatically)
#             self.update(key, value)
#         else:
#             if len(self.cache) == self.capacity:
#                 lfu_node = self.count[self.min_freq].removeTail()
#                 del self.cache[lfu_node.key]
#             self.min_freq = 1
#             node = ListNode(key, value)
#             self.count[self.min_freq].addNode(node)
#             self.cache[key] = node
                             
    
    
#     def update(self, key, val):
#         node = self.cache[key]
#         freq = node.freq
#         self.count[freq].removeNode(node)
        
#         node.val = val
#         node.freq += 1
#         self.count[node.freq].addNode(node)
#         # if the node's prev freq is the min_freq, and self.count[self.min_freq] only contains this node
#         # min_freq increases by one (node.freq is increased)
#         # self.count[prev_freq] can be deleted (the new freq & node has been added already)
#         if freq == self.min_freq and self.count[freq].size == 0:
#             del self.count[freq]
#             self.min_freq+=1 