class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d=defaultdict(list)
        
        for vote in votes:
            for i, char in enumerate(vote):
                if char not in d:
                    d[char]=[0]*len(vote)
                d[char][i]+=1
        
        names=sorted(votes[0])
        return ''.join(sorted(names, key=d.get, reverse=True))
        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # Time: O(N*S + Nlog(N)) => O(Nlog(N)) where N is the number of votes, and S is the length of each vote. There're only 26 chars so Max(S) is 26, constant O(1)
        
#         # Space: O(N*S) => O(N)
        
#         d = dict()
        
#         for vote in votes:
#             for i, char in enumerate(vote):
#                 if char not in d:
#                     d[char]=[0]*len(vote)
#                 d[char][i]+=1
                
#         names=sorted(d.keys())
#         return ''.join(sorted(names, key=lambda x:d[x], reverse=True))
        
                
        
        
        
        
        