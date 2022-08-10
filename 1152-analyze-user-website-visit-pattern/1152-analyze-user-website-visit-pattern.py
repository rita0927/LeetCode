class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        history = defaultdict(list)
        
        for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: x[1]):
            history[user].append(site)
            
        patterns = Counter()
        
        for user, sites in history.items():
            patterns.update(Counter(set(combinations(sites, 3))))
        
        return max(sorted(patterns), key = patterns.get)
        