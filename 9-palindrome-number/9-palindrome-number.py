class Solution:
    def isPalindrome(self, x: int) -> bool:
        nx = 0
        remainder = x
        if x < 0:
            return False
        if x < 10:
            return True
        
        while remainder: 
            temp = remainder%10 
            nx = nx * 10 + temp
            remainder = remainder//10
            
            if nx == x:
                return True
            
        return False 
        
        