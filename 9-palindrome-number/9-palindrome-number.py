class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        if x < 10:
            return True
        
        rem = x
        nx = 0
        
        while rem:
            nx = nx * 10 + rem%10
            rem = rem//10
        return nx == x
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        