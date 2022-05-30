class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        
        for word in strs:
            lst = [0] * 26
            for ch in word:
                i = ord(ch) - ord('a')
                lst[i] +=1
            res[tuple(lst)].append(word)
        
        return res.values()
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(NKlogK) where N is the length of strs and K is the maximum length of individual string
        
#         res = defaultdict(list)
        
#         for word in strs:
#             sortedWord = sorted(word)
#             # sorted convert string to list
#             # list can't be hashed, need to convert to tuple
#             res[tuple(sortedWord)].append(word)
#         return res.values()
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = defaultdict(list)
#         for word in strs:
#             count = [0] * 26
            
#             for ch in word:
#                 index = ord(ch) - ord('a')
#                 count[index] +=1
#             res[tuple(count)].append(word)
#         return res.values()
            
        
        
        
        
        