from heapq import *

class Leaderboard:

    def __init__(self):
        self.board = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score
        

    def top(self, K: int) -> int:
        
        heap = []
        for score in self.board.values():
            heapq.heappush(heap, score)
            if len(heap) > K:
                heapq.heappop(heap)
        return sum(heap)

     

    def reset(self, playerId: int) -> None:
        del self.board[playerId]

        
        
        
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)










# class Leaderboard:

#     def __init__(self):
#         self.board = defaultdict(int)
        

#     def addScore(self, playerId: int, score: int) -> None:
#         self.board[playerId] += score
        
#     # O(N)
#     def top(self, K: int) -> int:
#         scores = list(self.board.values())
#         K = len(scores) - K
        
#         def quickSelect(l,r):
#             pivot_index = random.randint(l,r)
#             pivot = scores[pivot_index]
            
#             scores[r], scores[pivot_index] = scores[pivot_index], scores[r]
#             p = l
            
#             for i in range(l,r):
#                 if scores[i] < pivot:
#                     scores[p], scores[i] = scores[i], scores[p]
#                     p += 1
#             scores[p], scores[r] = scores[r], scores[p]
            
#             if K< p:
#                 return quickSelect(l, p - 1)
#             elif K> p:
#                 return quickSelect(p + 1, r)
#             else:
#                 return 
        
        
#         quickSelect(0, len(scores) - 1)
#         return sum(scores[K:])
        
#     def reset(self, playerId: int) -> None:
#         del self.board[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)



# class Leaderboard:

#     # Space: O(N) + O(K) where O(N) for dict and O(K) for heap 
    
#     def __init__(self):
#         self.board = defaultdict(int)
        

#     def addScore(self, playerId: int, score: int) -> None:
#         self.board[playerId] += score
        
#     # Time: O(K + (N-K) * log(K)) where O(K) to construct the initial heap, for the rest of the (N-K) elements, push-pop requires log(K) for each element. If N >> K, then the final time complexity is O(NlogK)
    
#     def top(self, K: int) -> int:
#         # heap = list(self.board.values())
#         # return sum(heapq.nlargest(K, heap))
        
        
#         heap = []
#         for score in self.board.values():
#             heapq.heappush(heap, score)
#             if len(heap) > K:
#                 heapq.heappop(heap)
#         return sum(heap)
        

#     def reset(self, playerId: int) -> None:
#         del self.board[playerId]
        


    
    


# class Leaderboard:
    
#     # space: O(N)
#     def __init__(self):
#         self.board = defaultdict(int)
        
#     # time: O(1)
#     def addScore(self, playerId: int, score: int) -> None:
#         self.board[playerId] += score
        
#     # time: O(NlogN)
#     def top(self, K: int) -> int:
#         values = sorted(self.board.values(), reverse = True)
#         return sum(values[:K])
        
#     # time: O(1)
#     def reset(self, playerId: int) -> None:
#         del self.board[playerId]
        
