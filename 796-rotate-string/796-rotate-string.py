class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s+s 
        
#         for i in range(len(s)):
#             if len(s) !=len(goal):
#                 return False
            
#             if s[i:] + s[:i] == goal:
#                 return True
#         return False
    

