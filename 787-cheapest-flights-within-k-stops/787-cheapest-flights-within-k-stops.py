class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # either use dict or lst for the adj list 
        adj = [[]for _ in range(n)]
        # keep track of the min cost to each city 
        res = [float('inf') for _ in range(n)]
        # start city has the cost of 0
        res[src] = 0
        
        for s,e,c in flights:
            adj[s].append((e,c))
        
        # initialize the queue with src, available stops and the cost
        queue = deque([(src, k, 0)])
        while queue:
            # cost of the current accumulated path 
            s,stop,cost = queue.popleft()
            
            # add another layer of dest when stop = 0
            if stop < 0:
                continue
                
            for e,c in adj[s]:
                # only add the next city if the total cost is less than the current res[next_city]
                if cost + c < res[e]:
                    res[e] = cost + c
                    queue.append((e,stop-1,cost+c))
        # if the dst is never reached/updated, res[dst] is still float('inf')
        return res[dst] if res[dst] != float('inf') else -1 
                
            
        
            
        