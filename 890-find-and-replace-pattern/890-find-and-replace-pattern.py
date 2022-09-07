class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def match(word):
            d = {}
            for w, p in zip(word, pattern):
                if d.setdefault(w,p) != p:
                    return False
            return len(set(d.values())) == len(d.values())
        
        return filter(match, words)
                
                
            
        