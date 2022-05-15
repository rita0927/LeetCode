class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz", 
        }
        
        if not digits:
            return []
        
        res = []
        
        def backtrack(index, path):
            if index == len(digits):
                res.append(path)
                return
            
            digit = digits[index]
            for ch in dic[digit]:
                backtrack(index + 1, path+ch)
        
        backtrack(0, '')
        return res 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     
#     # Time: o(4 ^ N * N) where N is the length of digits, 4 refers to the max length of characters for each digit. Last N is the length of each output string (same as digits legnth), 4 ^ N is the number of output strings. 
#     # Space: O(N) due to the recursion call stack    
        
        
#         dic = {
#             '2': "abc",
#             '3': "def",
#             '4': "ghi",
#             '5': "jkl",
#             '6': "mno",
#             '7': "pqrs",
#             '8': "tuv",
#             '9': "wxyz", 
#         }
        
#         if not digits:
#             return []
        
#         res = []
        
#         def backtrack(index, path):
#             if index == len(digits):
#                 res.append(''.join(path))
#                 return
            
#             digit = digits[index]
#             for ch in dic[digit]:
#                 path.append(ch)
#                 backtrack(index + 1, path)
#                 path.pop()
#         backtrack(0, [])
#         return res 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
        
#         def backtrack(digits, sub):
            
#             if not digits:
#                 res.append(sub)
#                 return
            
#             digit = digits[0]
#             for ch in dic[digit]:
#                 backtrack(digits[1:], sub + ch)
#             digits = digit + digits
        
#         backtrack(digits, '')
#         return res 
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(digits) == 0:
#             return []

#         digitsMap = {
#             '2': "abc",
#             '3': "def",
#             '4': "ghi",
#             '5': "jkl",
#             '6': "mno",
#             '7': "pqrs",
#             '8': "tuv",
#             '9': "wxyz",
#         }
#         result = []

#         def backtrack(index, curStr):
#             if len(curStr) == len(digits):
#                 result.append(curStr)
#                 return

#             for letter in digitsMap[digits[index]]:
#                 backtrack(index + 1, curStr + letter)

#         backtrack(0, "")
#         return result