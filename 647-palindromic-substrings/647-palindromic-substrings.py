class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def countPalindrom(l,r):
            count = 0
            
            while l >= 0 and r < len(s) and s[l]==s[r]:
                count +=1
                l-=1
                r+=1
            return count
        
        for i in range(len(s)):
            # two senarios for palindrome:
            
            # odd number: single letter as the center
            res += countPalindrom(i, i)
            
            # even number: pair of letters as the center
            res += countPalindrom(i, i+1)
        return res 
            
            