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
        
        def backtrack(digits, sub):
            
            if not digits:
                res.append(sub)
                return
            
            digit = digits[0]
            for ch in dic[digit]:
                backtrack(digits[1:], sub + ch)
            digits = digit + digits
        
        backtrack(digits, '')
        return res 
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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