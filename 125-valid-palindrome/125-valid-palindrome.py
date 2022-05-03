class Solution:
    def isPalindrome(self, s: str) -> bool:
  
        # O(n), O(1)
    
        l = 0
        r = len(s) - 1
        
        while l < r:
            if not s[l].isalnum():
                l +=1
                continue
            if not s[r].isalnum():
                r -=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            
            l +=1
            r -=1
        return True 
        
        
        
        
        
        
        
#        # O(n), O(n) 
        
#         new_s = [ch.lower() for ch in s if ch.isalnum()]
#         new_s= "".join(new_s)
        
#         l = 0
#         r = len(new_s) - 1
        
#         # while l <r:
#         #     if new_s[l] == new_s[r]:
#         #         l +=1
#         #         r -=1
#         #     else:
#         #         return False
#         # return True
        
#         return new_s == new_s[::-1]
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
#         string = "".join([i for i in s if i.isalpha() or i.isnumeric()]).lower()
        
#         if len(string) == 1:
#             return True
        
#         left = 0
#         right = len(string) - 1

#         while left <= right:
#             if string[left] != string[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
        