class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.lst = []


    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.lst)
        self.lst.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        
        index = self.dic[val]
        last = self.lst[-1]
        self.lst[index] = last
        self.dic[last] = index
        self.lst.pop()
        del self.dic[val]
        return True
            


    def getRandom(self) -> int:
        return random.choice(self.lst)

        


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