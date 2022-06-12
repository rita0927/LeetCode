class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                string = ''
                while stack[-1] != '[':
                    string = stack.pop() + string 
                stack.pop()
                count = ''
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count 
                
                stack.append(string * int(count))
                
        return ''.join(stack)

                    
        
   

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# # Time: O(n) as every element in the string is visited exactly once
# # Space: O(nkm) Let the max size of a string within the parenthesis is n. for ex: "abc". Let the max number for string multiplication/count is 'k' and there are at the most 'm' of these. for ex: "3[abc]"


# In that case, the upper bound on space has to be O(nkm).
        
#         stack = []
        
#         for i in s:
            
#             if i != ']':
#                 stack.append(i)
#             else:
#                 substr = ''
                
#                 while stack[-1] !='[':
#                     substr = stack.pop() + substr
#                 # there's '[' before the string and number in the stack, pop out the '[' before start popping out the count 
#                 stack.pop()
#                 count = ''
#                 while stack and stack[-1].isdigit():
#                     count = stack.pop() + count
                
#                 stack.append(int(count) * substr)
#         return ''.join(stack)
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# # Time complexity: O(maxK^( countK) * n) where maxK is the max value of digit/count, countK is the number of nested brackets, and n is the max length of the string. ex, 20[a10[bc]], maxK is 20, countK is 2 due to 2 nested brackets, n is 2 due to max string length (bc)

# # Space complexity: 
        
#         string = ''
#         count = 0
#         stack = []
        
        
#         for i in s:
#             if i.isdigit():
#                 count = count * 10 + int(i)
#             elif i =='[':
#                 stack.append(string)
#                 string = ''
#                 stack.append(count)
#                 count = 0 
#             elif i == ']':
#                 num = stack.pop()
#                 prev = stack.pop()
#                 string = prev + num * string
#             else:
#                 string += i
            
#         return string 
                
                
                