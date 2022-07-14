from functools import lru_cache
class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words = set(wordDict)
        
        dp = [False] * (len(s) + 1)
        
        dp[0] = True
        

        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] in words and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         words = set(wordDict)
#         n = len(s)
#         dp = [False] * (n+1)
#         dp[0] = True
        
#         for i in range(1,n+1):
#             for j in range(i):
#                 if dp[j] and s[j:i] in words:
#                     dp[i] = True
#                     break
#         return dp[n]
            
        
        
        



#         word_set = set(wordDict)
#         q = deque([0])
#         visited = set()
#         while q:
#             start = q.popleft()
#             if start == len(s):
#                 return True
#             if start in visited:
#                 continue
#             visited.add(start)
#             for end in range(start + 1, len(s) + 1):
#                 if s[start:end] in word_set:
#                     q.append(end)
 
#         return False    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # O(n^3), O(n)
        # # to avoid TLE, add the index to visited set before append to the queue
        # words = set(wordDict)
        # visited = set()
        # visited.add(0)
        # queue = deque([0])
        # while queue:
        #     l = queue.popleft()
        #     if l == len(s):
        #         return True
        #     for r in range(l+1, len(s)+1):
        #         if r not in visited and s[l:r] in words:
        #             visited.add(r)
        #             queue.append(r)
        # return False 


        
     
        
        
        
        
        
        
      
        
        
        
#         d = set(wordDict)
        
#         dp = [False] * (len(s) + 1)
#         dp[0] = True
        
#         for i in range(1, len(s) + 1):
#             for j in range(i):
#                 if dp[j] and s[j:i] in d:
#                     dp[i] = True
#                     # break
#         return dp[len(s)]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # TLE!!!! O(n^3), O(n)
#         d = set(wordDict)
#         queue = deque([0])
#         visited = set()
        
#         while queue:
            
#             start = queue.popleft()
#             visited.add(start)
            
#             if start == len(s):
#                 return True
            
#             for end in range(start + 1, len(s) + 1):
#                 if s[start:end] in d and end not in visited:
#                     queue.append(end)
#         return False 
        
        
       
        
        
#         # O(n^3) and the worst case is O(n^2)
#         # O(n) depth of recursion tree
        
#         d = set(wordDict)
#         @lru_cache
#         def helper(start):
            
#             if start == len(s):
#                 return True
#            # range needs to include the len(s) to reach the base case
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