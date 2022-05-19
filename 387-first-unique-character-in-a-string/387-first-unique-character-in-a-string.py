class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# #O(N), O(1) because there're only 26 letters 

#         count = Counter(s)
#         for i, ch in enumerate(s):
#             if count[ch] == 1:
#                 return i
#         return -1
        
            
        