class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        
        for w in strs:
            count = [0] * 26
            for ch in w:
                count[ord(ch)-ord('a')]+=1 
            res[tuple(count)].append(w)
            
        return res.values()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         seen = defaultdict(list)
        
#         for w in strs:
#             sorted_word = sorted(w)
#             seen[''.join(sorted_word)].append(w)
#         return seen.values()
        
        
 
        
        
        
#         # O(NKlogK) where N is the length of strs and K is the maximum length of individual string. The outer loop has complexity O(N). We sort each string in O(KlogK) time.

#        # space O(NK)
        
#         res = defaultdict(list)
        
#         for word in strs:
#             sortedWord = sorted(word)
#             # sorted convert string to list
#             # list can't be hashed, need to convert to tuple
#             res[tuple(sortedWord)].append(word)
#         return res.values()
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
#          # O(Nk), O(Nk)       
        
#         res = defaultdict(list)
#         for word in strs:
#             count = [0] * 26
            
#             for ch in word:
#                 index = ord(ch) - ord('a')
#                 count[index] +=1
#             res[tuple(count)].append(word)
#         return res.values()
            
        
        
        
        
        