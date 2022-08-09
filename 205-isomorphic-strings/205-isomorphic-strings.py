class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        zip_set = set(zip(s,t))
        return len(zip_set) == len(set(s)) == len(set(t))
        
       