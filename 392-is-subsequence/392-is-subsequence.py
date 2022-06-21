class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s:
            return True 
        
        s_idx = 0
        for ch in t:
            if ch == s[s_idx]:
                s_idx += 1
            
            if s_idx == len(s):
                return True
            
        return False 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = defaultdict(list)
#         for i, ch in enumerate(t):
#             d[ch].append(i)
        
#         # stores the index of the target string where we found the previous character match
#         cur = -1
        
#         for ch in s:
#             if ch not in d:
#                 return False 
#             lst = d[ch]
#             match_idx = bisect_right(lst, cur)
            
#             if match_idx != len(lst):
#                 cur = lst[match_idx]
#             else:
#                 return False 
            
#         return True 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # for the edge case of s == ''
#         if not s:
#             return True   
#         i = 0
#         for j in range(len(t)):

#             if s[i] == t[j]:
#                 i += 1        
#             if i == len(s):
#                 return True
            
#         return False 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(T) where T is the length of the target string (t). Has to iterate the entire target string. Even when the souce string is longer, iteration stops when target string is exhasted. 
#         # O(T) due to the call stack
#         def helper(s_idx, t_idx):
            
#             if s_idx == len(s):
#                 return True
#             if t_idx == len(t):
#                 return False 
            
#             if s[s_idx] == t[t_idx]:
#                 s_idx += 1
#             t_idx += 1
#             return helper(s_idx, t_idx)
        
#         return helper(0,0)
            
            
        
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(s) == 0:
#             return True
        
#         if len(s) > len(t):
#             return False
        
#         s_index = t_index= 0
        
#         while t_index < len(t) and s_index <len(s):
#             if t[t_index] == s[s_index]:
#                 s_index +=1
#             t_index+=1
        
#         return s_index == len(s)
            
        
        