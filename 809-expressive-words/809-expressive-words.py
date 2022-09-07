class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def compress(w):
            letters = []
            counts = []
            
            for ch in w:
                if not letters or ch != letters[-1]:
                    letters.append(ch)
                    counts.append(1)
                else:
                    counts[-1]+=1
                    
            return letters, counts
        
        s_letters, s_counts = compress(s)
        
        def is_stretchy(w):
            w_letters, w_counts = compress(w)
            
            if w_letters != s_letters:
                return False
            
            for i in range(len(w_counts)):
                if s_counts[i] < 3 and s_counts[i] != w_counts[i]:
                    return False
                
                if w_counts[i] > s_counts[i]:
                    return False
            return True
                
        res = 0
        for w in words:
            if is_stretchy(w):
                res +=1
                
        return res 
            
            
                    
        