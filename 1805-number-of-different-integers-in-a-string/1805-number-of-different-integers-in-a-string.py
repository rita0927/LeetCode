class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        res = set()
        num = ''
        
        for i, w in enumerate(word):
            if w.isdigit():
                num += w
                
            if not w.isdigit() or i == len(word)-1:
                if num:
                    res.add(int(num))
                num = ''
        return len(res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = set()
#         num = []
#         for i,w in enumerate(word):
#             if w.isdigit():
#                 num.append(w)
                
#             if not w.isdigit() or i == len(word) - 1:
#                 if num:
#                     while num and num[0] == '0':
#                         num.pop(0)
#                     res.add(''.join(num))
#                     num = []

            
#         return len(res)
                    
            
        