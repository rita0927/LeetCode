class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        
        for s in strs:
            while not s.startswith(pre):
                pre = pre[:-1]
        return pre 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(strs) == 1:
#             return strs[0]
        
#         min_str = min(strs)
#         max_str = max(strs)
#         length= min(len(min_str), len(max_str))
#         i = 0
        
#         while i < length:
#             if min_str[i] != max_str[i]:
#                 break
#             i+=1 
#         return min_str[:i]
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(m*n)  where n is the number of strings and m is the len of string; or O(S) where S is the sum of all characters in all strings
#         pre = strs[0]

#         for s in strs:
#             while not s.startswith(pre):
#                 pre = pre[:-1]
#         return pre
                
        