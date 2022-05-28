import itertools

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        # O(N), O(1)
        def helper(string):
            skip = 0
            
            for ch in reversed(string):
                if ch == '#':
                    skip += 1
                elif skip:
                    skip -=1
                else:
                    yield ch
        
        # zip_longest zip up two strings/lists that match the length of longest one
        # the missing element is filled with None
        for ch1, ch2 in itertools.zip_longest(helper(s), helper(t)):
            if ch1 != ch2:
                return False
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def helper(string):
#             stack = []
#             for i in string:
#                 if stack and i == '#':
#                     stack.pop()
#                 elif i != '#':
#                     stack.append(i)
                    
#             return ''.join(stack)
        
#         return helper(s) == helper(t)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def helper(string):
#             stack = []
            
#             for i in string:
#                 if i != '#':
#                     stack.append(i)
#                 # i == '#' and stack is not empty
#                 elif stack:
#                     stack.pop()

#             return ''.join(stack)
                    
#         return helper(s) == helper(t)
        
        