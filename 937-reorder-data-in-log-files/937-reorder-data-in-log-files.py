class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        ll = []
        dl = []
        
        for log in logs:
            log = log.split()
            if log[1].isdigit():
                dl.append(' '.join(log))
            else:
                ll.append(log)
        
        ll.sort(key = lambda x: (x[1:], x[0]))
        ll = [' '.join(l) for l in ll]
        return  ll + dl
            
            
        