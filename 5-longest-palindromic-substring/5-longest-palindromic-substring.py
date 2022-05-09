class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        def isPalindrome(l,r):
            while l >=0 and r <len(s) and s[l] == s[r]:
                l -=1
                r +=1
            return s[l+1:r]
        
        for i in range(len(s)):
            odd = isPalindrome(i, i)
            even = isPalindrome(i, i+1)
            
            if len(odd) > len(even):
                res = odd if len(odd) > len(res) else res 
            else:
                res = even if len(even) >len(res) else res
        
        return res 

            
        

            
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
            
        
#         res = ''
        
#         for i in range(len(s)):
            
#             l,r = i, i
        
#             while l >=0 and r <len(s) and s[l] == s[r]:
#                 if len(res) < r - l + 1:
#                     res = s[l: r+ 1]
                    
#                 l-=1
#                 r+=1
            
#             l, r = i, i+ 1
            
#             while l >=0 and r < len(s) and s[l] == s[r]:
#                 if len(res) < r-l + 1:
#                     res = s[l: r+1]
#                 l-=1
#                 r+=1
                    
#         return res

            
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

       
        












      
#         res = ''
#         resLen = 0
        
        
#         for i in range(len(s)):
#             l,r = i, i 
#             while l>=0 and r <len(s) and s[l] == s[r]:
#                 if resLen < r-l +1:
#                     res = s[l: r+1]
#                     resLen = r-l+1
#                 l-=1
#                 r+=1
                
#             l, r = i, i+1
#             while l >=0 and r<len(s) and s[l] == s[r]:
#                 if resLen < r-l +1:
#                     res = s[l:r+1]
#                     resLen = r-l+1
#                 l-=1
#                 r+=1
            
#         return res
            
# O(n^2), O(1)
            
                  
        
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        res = ""
        for i in range(len(s)):
            test = helper(i, i)
            if len(test) > len(res):
                res = test
            test = helper(i, i + 1)
            if len(test) > len(res):
                res = test
        return res

        