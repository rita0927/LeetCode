class Solution:
    
    def addBoldTag(self, s: str, words: List[str]) -> str:

        n = len(s)
        trie = {}
        word_key = 'isWord'
        
        for w in words:
            node = trie
            for ch in w:
                node = node.setdefault(ch, {})
            node[word_key] = True 
        
        intervals = []
        for l in range(n):
            node = trie
            for r in range(l,n):
                if not s[r] in node:
                    break
                node = node[s[r]]
                if word_key in node:
                    if intervals and intervals[-1][1] >= l:
                        intervals[-1][1] = max(r+1, intervals[-1][1])
                    else:
                        intervals.append([l, r+1])
        
        res = ''
        prev = 0
        for start, end in intervals:
            res += s[prev:start] + '<b>' + s[start:end] + '</b>'
            prev = end 
        return res + s[prev:]
            
            
        
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         trie = {}
#         word_key = 'isWord'
        
#         for word in words:
#             node = trie
#             for ch in word:
#                 node = node.setdefault(ch, {})
#             node[word_key] = True 
        
#         intervals = []
#         for l in range(len(s)):
#             node = trie
#             for r in range(l,len(s)):
#                 if s[r] not in node:
#                     break
#                 node = node[s[r]]
#                 if word_key in node:
#                     if intervals and intervals[-1][1] >= l:
#                         intervals[-1][1] = max(r + 1, intervals[-1][1])
#                     else:
#                         intervals.append([l,r+1])
#         res = ''
#         prev= 0
        
#         for start,end in intervals:
#             res += s[prev:start] + '<b>' + s[start:end] + '</b>' 
#             prev = end 
#         return res + s[prev:]
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(s)
#         buckets = [False] * n
        
#         intervals = []
#         for l in range(len(s)):
#             r = 0
#             for w in words:
#                 if s.startswith(w,l):
#                     r = max(r, l+len(w))
#             for i in range(l,r):
#                 buckets[i] = True 
#         res = ''
#         for i in range(len(s)):
#             if buckets[i] and (i == 0 or not buckets[i-1]):
#                 res += '<b>'
#             res += s[i]
#             if buckets[i] and (i == n-1 or not buckets[i+1]):
#                 res += '</b>'
#         return res 
                
        
        
        
        
 
    
    
    
    

    
    
    
    
    
    
    
    
    
# #     No of words = m, Length of largest word = k, Length of s = n

# #     O(m*k) - trie build
# #     O(n * k) - search & match 
# #     O(n) - merge & put bold characters
# #     total: O(nk + mk)
    
#     def addBoldTag(self, s: str, words: List[str]) -> str:
#         word_key = 'isWord'
#         trie = {}
#         n =len(s)

#         for w in words:
#             node = trie
#             for ch in w:
#                 node = node.setdefault(ch, {})
#             node[word_key] = True 
  
#         intervals = []
#         for i in range(n):
#             node = trie
#             r = 0
            
#             for l in range(i,n):
#                 if s[l] not in node:
#                     break
#                 node = node[s[l]]
#                 if word_key in node:
#                     # reach the end of the word, the index of the last ch in the word is l
#                     # the range of word is [i,r)
#                     r = max(r, l+1)
#             # if r has been updated (find at least one word), otherwise r == 0 
#             if r:
#                 # if starting of new interval i is overlapping the last saved interval
#                 # last[end] >= new[start], the last end is exclusive 
#                 if intervals and intervals[-1][1] >= i:
#                     intervals[-1][1] = max(r, intervals[-1][1])
#                 else:
#                     intervals.append([i,r])
 
#         res = ''      
#         prev = 0
        
#         for start, end in intervals:
#             res += s[prev:start] + '<b>' + s[start:end] + '</b>'
#             prev = end
#         return res + s[prev:]
        
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# O(MNK) where M = len(s), N = len(words), K = max len of word in words       
        
#         n = len(s)
#         buckets = [False] * n
#         l = 0
        
#         for l in range(n):
#             r = 0
#             for w in words:
#                 if s.startswith(w,l):
#                     r = max(r, l+len(w))
#             for i in range(l,r):
#                 buckets[i] = True 
            
        
#         res = ''
        
#         for i in range(n):
#             if buckets[i] and (i == 0 or i >0 and not buckets[i-1]):
#                 res += '<b>'
#             res += s[i]
#             if buckets[i] and (i == n-1 or i < n - 1 and not buckets[i+1]):
#                 res += '</b>'
#         return res 
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(s)
#         # mark all ch as False, update to True if it's contained in the word 
#         buckets = [False] * n
        
#         r = 0
#         for l in range(n):
#             for w in words:
#                 # if s[l:] starts with w
#                 if s.startswith(w,l):
#                     # find/update the end, so the range [l,r) need to be updated to True
#                     r = max(r,l+len(w))
#             # update the buckets for [l,r) to True
#             for i in range(l,r):
#                 buckets[i] = True
            
#         res = ''

#         for i in range(n):
#             # if the first ch is marked as True OR prev ch is False and cur is True 
#             if (i == 0 and buckets[i]) or (i > 0 and buckets[i] and not buckets[i-1]):
#                 res += '<b>'
#             res += s[i]
#             # if the last ch is marked as True OR next is False and cur is True 
#             if (i == n-1 and buckets[i]) or (i < n-1 and buckets[i] and not buckets[i+1]):
#                 res += '</b>'
        
#         return res 
                    
        
        
        
        
        
        
        
        
        
   
            
            
                
        