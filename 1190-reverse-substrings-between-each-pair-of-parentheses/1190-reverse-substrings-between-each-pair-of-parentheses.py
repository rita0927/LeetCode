class Solution:
    def reverseParentheses(self, s: str) -> str:
        opens = []
        i = 0
        
        while i < len(s):
            if s[i] == "(":
                opens.append(i)
                i+=1
            elif s[i] == ")":
                start = opens.pop()
                sub = s[start + 1:i]
                sub = sub[::-1]
                s = s[:start] + sub + s[i + 1:]
                i-=1
            else:
                i +=1
                
        return s
        