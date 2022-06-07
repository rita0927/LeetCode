class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        
        index = len(self.arr)
        self.map[val] = index
        self.arr.append(val)
        return True 


    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        index = self.map[val]
        last = self.arr[-1]
        
        self.arr[index] = last
        self.map[last] = index
        self.arr.pop()
        del self.map[val]
        return True 
        
        


    def getRandom(self) -> int:
        return random.choice(self.arr)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()















# class RandomizedSet:

#     def __init__(self):
#         self.dict = {}
#         self.list = []
        

#     def insert(self, val: int) -> bool:
#         if val in self.dict:
#             return False
#         self.dict[val] = len(self.list)
#         self.list.append(val)
#         return True
        

#     def remove(self, val: int) -> bool:
#         if val not in self.dict:
#             return False
#         last = self.list[-1]
#         index = self.dict[val]
#         self.list[index] = last
#         self.list.pop()
#         self.dict[last] = index
#         del self.dict[val]
#         return True
        

#     def getRandom(self) -> int:
#         return choice(self.list)