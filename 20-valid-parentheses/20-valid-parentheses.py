class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        
        stack = []
        
        for i in s:
            if not stack or i not in dic:
                stack.append(i)
            else:
                if stack.pop() != dic[i]:
                    return False

        return True if not stack else False 