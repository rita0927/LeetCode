class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        ans = ''
        # get the sum of the shift from last to first
        shift = 0
        
        for i in range(len(s) - 1, -1, -1):
            ans = chr((ord(s[i]) - ord('a') + shift +shifts[i]) % 26 + ord('a')) + ans
            shift += shifts[i]
        return ans
            
            
#         for i in range(len(s)):
#             sub = s[:i + 1]
#             for j in range(len(sub)): 
#                 pre = chars[sub[j]]
#                 post = (pre + shifts[i]) % 26
#                 sub[j] = letters[post]
#             s[:i+1] = sub
            
#         return "".join(s)

        
        
        
        
        