class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            if not stack or a * stack[-1] > 0 or a > 0:
                stack.append(a)
            else:
                while stack and abs(a)> abs(stack[-1]) and stack[-1] > 0:
                    stack.pop()
                if stack and stack[-1] == -a:
                    stack.pop()
                elif not stack or a * stack[-1] > 0:
                    stack.append(a)
        return stack
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stack = []

#         while stack and a < 0 < stack[-1]:
#             if stack[-1] < -a:
#                 stack.pop()
#                 continue
#             elif stack[-1] == -a:
#                 stack.pop()
#             break
#         else:
#             stack.append(a)

#         return stack
                
        