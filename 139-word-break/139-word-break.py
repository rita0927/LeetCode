from functools import lru_cache
class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        d = set(wordDict)
        @lru_cache
        def helper(start):
            
            if start == len(s):
                return True
                
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in d and helper(end):
                    return True
            return False
        return helper(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = set(wordDict)
        
#         def helper(start):
#             if start == len(s):
#                 return True
            
#             for end in range(start + 1, len(s) + 1):
#                 if s[start:end] in d and helper(end):
#                     return True
#             return False
#         return helper(0)
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = set(wordDict)
#         N = len(s)

#         dp = [False for _ in range(N + 1)]  # N+1 to include the base case dp[0]
#         dp[0] = True

#         for start in range(N):
#             if not dp[start]:
#                 continue
#             for end in range(start + 1, N + 1):
#                 if s[start:end] in d:
#                     dp[end] = True
#         return dp[-1]