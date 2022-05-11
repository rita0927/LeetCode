class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if len(s) < 2: return len(s)
         
    # O(26n) results in O(n)
    # O(1)
        count = defaultdict(int)
        res = 0
        l = 0
        maxFreq = 0
        
        for r in range(len(s)):
            count[s[r]]+=1
            maxFreq = max(maxFreq, count[s[r]])
            
            # occurance of the most frequent letter + k results in the longest res 
            # when window width - occurance of most frequent letter > k, need to move left pointer
            if (r-l+1) - maxFreq > k:
                # decrease the l pointer occurance before moving the pointer
                count[s[l]] -=1
                l+=1
            res = max(res, r-l+1)
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    

    
#     def characterReplacement(self, s: str, k: int) -> int:
         
#     # O(26n) results in O(n)
#     # O(1)
#         count = defaultdict(int)
#         res = 0
#         l = 0
        
#         for r in range(len(s)):
#             count[s[r]]+=1
            
#             # occurance of the most frequent letter + k results in the longest res 
#             # when window width - occurance of most frequent letter > k, need to move left pointer
#             while (r-l+1) - max(count.values()) > k:
#                 # decrease the l pointer occurance before moving the pointer
#                 count[s[l]] -=1
#                 l+=1
#             res = max(res, r-l+1)
#         return res 