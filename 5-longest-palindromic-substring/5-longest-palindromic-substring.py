class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ''
        
        def helper(l,r):
            nonlocal res 
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = s[l:r+1] if len((res)) < (r-l+1) else res 
                l -= 1
                r += 1        
        
        for i in range(len(s)):
            helper(i,i)
            helper(i,i+1)
        return res 


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = ""
        
#         def isPalindrome(l,r):
#             nonlocal res 
#             while l >=0 and r <len(s) and s[l] == s[r]:
#                 l -=1
#                 r +=1
#             res = s[l + 1:r] if (r-l-1) > len(res) else res 
        
#         for i in range(len(s)):
#             isPalindrome(i, i)
#             isPalindrome(i, i+1)
            
        
#         return res 

            
        

            
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
            
        
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
            
                  
        
#         def helper(l, r):
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 l -= 1
#                 r += 1
#             return s[l + 1: r]

#         res = ""
#         for i in range(len(s)):
#             test = helper(i, i)
#             if len(test) > len(res):
#                 res = test
#             test = helper(i, i + 1)
#             if len(test) > len(res):
#                 res = test
#         return res

        