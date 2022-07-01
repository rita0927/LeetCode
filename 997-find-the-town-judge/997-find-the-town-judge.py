class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        judges  = defaultdict(int)
        people = set()
        
        for p, j in trust:
            people.add(p)
            judges[j] +=1

        res = None
        for j in judges:
            if judges[j] == n-1 and j not in people:
                if not res:
                    res = j
                else:
                    return -1
        return res if res else -1 
                
        
        