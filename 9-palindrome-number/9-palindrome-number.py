class Solution:
    def isPalindrome(self, x: int) -> bool:
        nx = 0
        cur = x
        if x < 0:
            return False
        if x < 10:
            return True
        
        while cur: 
            temp = cur%10 
            nx = nx * 10 + temp
            cur = cur//10
            
        return nx == x 
        
        