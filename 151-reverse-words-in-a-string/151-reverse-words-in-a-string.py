class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        # remove the leading space
        while l < len(s) and s[l] == ' ':
                l+=1
        # remove the tailing space
        while r >= 0 and s[r] == ' ':
            r -=1
            
        queue = deque()
        temp = ''
        
        while l <=r:
            if s[l] == ' ' and temp:
                queue.appendleft(temp)
                temp = ''
            elif s[l] != ' ':
                temp += s[l]
            l += 1
        
        if temp:
            queue.appendleft(temp)
        return ' '.join(queue)
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # return ' '.join(reversed(s.split()))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         s.strip()
#         res = []
#         temp = ''
        
#         for i in s:
#             if i == ' ':
#                 if temp:
#                     res.append(temp)
#                     temp = ''
#             else:
#                 temp += i
        
#         if temp:
#             res.append(temp)
        
#         return ' '.join(reversed(res))
                
        
        