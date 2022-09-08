class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def compress(word):
            letters, counts = [], []
            
            for ch in word:
                if not letters or ch != letters[-1]:
                    letters.append(ch)
                    counts.append(1)
                else:
                    counts[-1]+=1
            
            return letters, counts
        
        s_letters, s_counts = compress(s)
        
        def is_stretchy(word):
            w_letters, w_counts = compress(word)
            if s_letters != w_letters:
                return False 
            
            for i in range(len(w_letters)):
                if w_letters[i] != s_letters[i]:
                    return False
                if s_counts[i] < 3 and s_counts[i] != w_counts[i]:
                    return False
                if w_counts[i] > s_counts[i]:
                    return False
                
            return True 
        
        res = 0
        for word in words:
            if is_stretchy(word):
                res += 1
        return res 
                    
            
            
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def compress(w):
#             letters = []
#             counts = []
            
#             for ch in w:
#                 if not letters or ch != letters[-1]:
#                     letters.append(ch)
#                     counts.append(1)
#                 else:
#                     counts[-1]+=1
                    
#             return letters, counts
        
#         s_letters, s_counts = compress(s)
        
#         def is_stretchy(w):
#             w_letters, w_counts = compress(w)
            
#             if w_letters != s_letters:
#                 return False
            
#             for i in range(len(w_counts)):
#                 if s_counts[i] < 3 and s_counts[i] != w_counts[i]:
#                     return False
                
#                 if w_counts[i] > s_counts[i]:
#                     return False
#             return True
                
#         res = 0
#         for w in words:
#             if is_stretchy(w):
#                 res +=1
                
#         return res 
            
            
                    
        