class MyHashMap:

    def __init__(self):
        self.size = 2069
        self.data = [[] for _ in range(self.size)]
    
    def hash_function(self, key):
        return key % self.size 

    def put(self, key: int, value: int) -> None:
        
        hashed_key = self.hash_function(key)
        bucket = self.data[hashed_key]
        
        for i in range(len(bucket)):
            k, v = bucket[i]
            if k == key:
                bucket[i][1] = value
                return
   
        bucket.append([key, value])
        

    def get(self, key: int) -> int:
        hashed_key = self.hash_function(key)
        bucket = self.data[hashed_key]
        
        for i in range(len(bucket)):
            k,v = bucket[i]
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        hashed_key = self.hash_function(key)
        bucket = self.data[hashed_key]
        
        for i in range(len(bucket)):
            k, v = bucket[i]
            
            if k == key:
                bucket.pop(i)
                return  













# # Without hashing 

# class MyHashMap:

#     def __init__(self):
#         self.data = [-1] * 1000001
        

#     def put(self, key: int, value: int) -> None:
#         self.data[key] = value

#     def get(self, key: int) -> int:
#         return self.data[key]

#     def remove(self, key: int) -> None:
#         self.data[key] = -1
    
    
    
    
    
    
    
    
    
        
# class MyHashMap:

#     def __init__(self):
#         self.size = 2069
#         self.buckets = [[] for _ in range(self.size)]
        
#     def getIndex(self, key):
        
#         # random hash function
#         hashResult = key % self.size
#         bucket = self.buckets[hashResult]
        
#         for i, (k,v) in enumerate(bucket):
#             if k == key:
#                 return bucket, i
#         return bucket, -1
        
        
#     def put(self, key: int, value: int) -> None:
#         bucket, index = self.getIndex(key)
        
#         if index < 0:
#             bucket.append((key, value))
#         else:
#             bucket[index] = (key, value)
        

#     def get(self, key: int) -> int:
#         bucket, index = self.getIndex(key)
#         if index < 0:
#             return -1
#         else:
#             return bucket[index][1]
        

#     def remove(self, key: int) -> None:
#         bucket, index = self.getIndex(key)
#         if index < 0:
#             return 
#         else:
#             bucket.pop(index)
        
        
        
        
        


# class MyHashMap:

#     def __init__(self):
        

#     def put(self, key: int, value: int) -> None:
        

#     def get(self, key: int) -> int:
        

#     def remove(self, key: int) -> None:
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)