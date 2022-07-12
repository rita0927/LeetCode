class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        d = {words[i]: i for i in range(len(words))}
        
        def isPalindrome(s):
            return s == s[::-1]
#             l = 0
#             r = len(s) - 1
            
#             while l < r:
#                 if s[l] != s[r]:
#                     return False
#                 l += 1
#                 r -= 1
#             return True 
        
        res = []
        
        # reflection in the d, ex: 'abc', 'cba'
        for w in words:
            reflected = w[::-1]
            # find the reflected string 
            # string itself is not a palindrome, ex. 'aba'
            if reflected in d and d[reflected] != d[w]:
                res.append([d[w], d[reflected]])
 
        # "" in the words, ex: 'a', ''
        if '' in d:
            for w in words:
                if w and isPalindrome(w):
                    res.append([d[w], d['']])
                    res.append([d[''], d[w]])
                

        # word1 + word2 is palindrome 
        for w in words:
            for i in range(1,len(w)):
                left = w[:i]
                right = w[i:]
                
                # ex: 'aaba', 'ab'
                if isPalindrome(left):
                    reversedRight = right[::-1]
                    if reversedRight != w and reversedRight in d:
                        res.append([d[reversedRight], d[w]])
                        
                # ex: 'abaa', 'ba'
                if isPalindrome(right):
                    reversedLeft = left[::-1]
                    if reversedLeft != w and reversedLeft in d:
                        res.append([d[w], d[reversedLeft]])
        return res 
                        
                        
                        
                        
                        
                        
                        
        