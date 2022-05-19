class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x< 0:
            return False
        
        n = 0 
        y = x
        while y:
            n = n* 10 + y%10
            y = y//10
        
        return n == x
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         nx = 0
#         remainder = x
#         if x < 0:
#             return False
#         if x < 10:
#             return True
        
#         while remainder: 
#             temp = remainder%10 
#             nx = nx * 10 + temp
#             remainder = remainder//10
            
#         return nx == x 
        
        