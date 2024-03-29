class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        words = set(wordDict)
        res = []
        
        def backtrack(index, path):
            if index == len(s):
                res.append(' '.join(path))
                return
            
            temp = ''
            for i in range(index, len(s)):
                temp += s[i]
                if temp in words:
                    path.append(temp)
                    backtrack(i+1, path)
                    path.pop()
                    
        backtrack(0, [])
        return res 
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(N^2+2^N+W) where N is the len of string, and W is len wor wordDict 
#         # O(2^N*N+W)
#         d = set(wordDict)
#         cache = {}
        
#         # either use cache or use functools.lru_cache
        
#         # @functools.lru_cache
#         def helper(s):
#             if s in cache:
#                 return cache[s]
#             res = []
#             for i in range(1, len(s) + 1):
#                 word = s[:i]
#                 if word in d:
#                     if len(s) == len(word):
#                         res.append(word)
#                     else:
#                         for words in helper(s[i:]):
#                             res.append(word + ' ' + words)
#             cache[s] = res 
#             return res 
        
#         return helper(s)
        
        
        
     
        
        
        
        
#         d = set(wordDict)
        
#         @functools.lru_cache
#         def helper(s):
#             res = []
            
#             for i in range(1, len(s) + 1):
#                 word = s[:i]
#                 if word in d:
#                     if len(s) == len(word):
#                         res.append(word)
#                     else:
#                         for w in helper(s[i:]):
#                             res.append(word + ' ' + w)
#             return res 
            
            
#             # for word in d:
#             #     if word == s[:len(word)]:
#             #         if len(s) == len(word):
#             #             res.append(word)
#             #         else:
#             #             for w in helper(s[len(word):]):
#             #                 res.append(word + ' ' + w)
#             # return res 
        
#         return helper(s)
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # cache = {}
        
#         @functools.lru_cache
#         def helper(s):
# #             if s in cache:
# #                 return cache[s]
            
#             res = []
            
#             for w in wordDict:
#                 if s[:len(w)] == w:
#                     if len(s) == len(w):
#                         res.append(w)
#                     else:
#                         for word in helper(s[len(w):]):
#                             res.append(w+' '+word)
#             # cache[s] = res

#             return res 
#         return helper(s)
            
                    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         d = set(wordDict)
#         res = []
        
#         def dfs(l, path):
            
#             if l == len(s):
#                 res.append(' '.join(path))
#                 return
            
#             for r in range(l+1, len(s) + 1):
#                 word = s[l:r]
#                 if word in d:
#                     dfs(r, path+[word])

#         dfs(0, [])
#         return res 
            
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# O(W + N^2 + 2^N) where N is the length of the string and W is the number of words in dictionary. O(W) to convert the wordDict to set.        
        
        
#         d = set(wordDict)
#         res = []
        
#         def backtrack(i, path):
#             if i == len(s):
#                 res.append(' '.join(path))
            
#             for j in range(i + 1, len(s) + 1):
#                 word = s[i:j]
#                 if word in d:
#                     path.append(word)
#                     backtrack(j, path)
#                     path.pop()
#         backtrack(0, [])
        
#         return res 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = set(wordDict)
#         res = []
        
#         def dfs(i, path):
#             if i == len(s):
#                 res.append(' '.join(path))
#                 return
            
#             for j in range(i+1, len(s) + 1):
#                 if s[i:j] in d:
#                     dfs(j, path + [s[i:j]])
#         dfs(0, [])
#         return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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


        