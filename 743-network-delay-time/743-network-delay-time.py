from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        
        for s,e,w in times:
            adj[s].append((e,w))
        
        heap = [(0,k)]
        res = 0
        visited = set()
        while heap:
            w1,n1 = heappop(heap)
            if n1 in visited:
                continue 
            visited.add(n1)
            res = max(res, w1)
            
            for n2,w2 in adj[n1]:
                if n2 not in visited:
                    heappush(heap, (w1+w2, n2))
        return res if len(visited) == n else -1
            
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(ElogV) where E is the number of edges and v is the number of Vectors
#         # O(V+E) where both adj and heap take O(E), visited takes O(V) space 
        
#         adj = defaultdict(list)
        
#         for s,e,t in times:
#             adj[s].append((e,t))
            
#         res = 0
#         heap = [(0,k)]
#         visited = set()
        
#         while heap:
#             t1,n1 = heapq.heappop(heap)
#             # if the node has been visited, there's a better path to get there quicker, no need to visit again
#             if n1 in visited:
#                 continue
#             visited.add(n1)
#             # update the result to get the max time for all the paths 
#             res = max(res, t1)
#             for n2,t2 in adj[n1]:
#                 if n2 not in visited:
#                     # can't add to visited here because the heap needs to sort all the nodes first 
#                     heapq.heappush(heap, (t1 + t2, n2))
        
#         return res if len(visited) == n else -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         edges = defaultdict(list)

#         for u, v, w in times:
#             edges[u].append((v, w))

#         minHeap = [(0, k)]
#         visit = set()
#         t = 0

#         while minHeap:
#             w1, n1 = heapq.heappop(minHeap)
#             if n1 in visit:
#                 continue
#             visit.add(n1)
#             t = max(t, w1)

#             for n2, w2 in edges[n1]:
#                 if n2 not in visit:
#                     heapq.heappush(minHeap, (w1 + w2, n2))

#         return t if len(visit) == n else -1 