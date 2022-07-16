class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        A = len(s1)
        B = len(s2)
        C = len(s3)
        if A+B != C: return False 
        
        @lru_cache 
        def helper(i1, i2, i3):
            
            if i3 == C:
                return True
            p1 = False
            p2 = False
            if i1 < A and s1[i1] == s3[i3]:
                p1 = helper(i1+1, i2, i3+1)
            if i2 < B and s2[i2] == s3[i3]:
                p2 = helper(i1, i2+1, i3+1)
            return p1 or p2 
        return helper(0,0,0)