class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        history = defaultdict(list)
        
        for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: x[1]):
            history[user].append(site)
        
        patterns = Counter()
        
        for user, sites in history.items():
            patterns.update(Counter(set(combinations(sites, 3))))
        print(patterns)
        return max(sorted(patterns), key = patterns.get)
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # {user: list of sites}
#         history = defaultdict(list)
        
#         # create tuple of (user, time, site) using zip
#         # sort by lambda: user (group by user), time (time is not sorted)
#         for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0], x[1])):
#             history[user].append(site)
        
#         patterns = Counter()
        
#         for user, sites in history.items():
#             # itertools.combinations generate combinations (maintain the element order)
#             # remove duplicate of combinations using set
#             # count the pattern for each user 
#             # Counter.update will update the val on each key 
#             patterns.update(Counter(set(combinations(sites, 3))))
        
#         # sort partterns keys in lexicographically order
#         # take the max with the key of patterns.get
#         return max(sorted(patterns), key = patterns.get)
        
        
        