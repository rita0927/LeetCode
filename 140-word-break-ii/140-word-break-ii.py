class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        d = set(wordDict)
        res = []
        
        def dfs(i, path):
            if i == len(s):
                res.append(' '.join(path))
            
            for j in range(i+1, len(s) + 1):
                if s[i:j] in d:
                    dfs(j, path + [s[i:j]])
        dfs(0, [])
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = set(wordDict)
#         res = []
        
#         def backtrack(i, path):
#             if i == len(s):
#                 res.append(' '.join(path))
#                 return

#             for j in range(i + 1, len(s) + 1):
#                 if s[i:j] in d:
#                     path.append(s[i:j])
#                     backtrack(j, path)
#                     path.pop()
#         backtrack(0, [])
        
#         return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d= set(wordDict)
#         res = set()
        
#         def backtrack(i, path):
#             if i == len(s):
#                 res.add(' '.join(path))
#                 return
#             for j in range(i+1, len(s)+1):
#                 if s[i:j] in d:
#                     path.append(s[i:j])
#                     backtrack(j, path)
#                     path.pop()
#         backtrack(0, [])
#         return res
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # check if ch in s is a subset of ch in wordDict
#         if set(Counter(s).keys()) > set(Counter(''.join(wordDict)).keys()):
#             return []
        
        
#         d = set(wordDict)
#         dp = [[]] * (len(s) + 1)
#         dp[0] = ['']
        
#         for i in range(1, len(s) + 1):
#             sublist = []
#             for j in range(i):
#                 word = s[j:i]
#                 if word in d:
#                     for sub in dp[j]:
#                         temp = (sub + ' ' + word).strip()
#                         sublist.append(temp)
#             dp[i] = sublist
              
#         return dp[len(s)]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
#         d = set(wordDict)

#         def dfs(index, path):
#             if index == len(s):
#                 res.append(" ".join(path))

#             for i in range(index, len(s)):
#                 tmp = s[index : i + 1]
#                 if tmp in d:
#                     dfs(i + 1, path + [tmp])

#         dfs(0, [])

#         return res


        