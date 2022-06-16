from heapq import *
class StockPrice:

    def __init__(self):
        self.records = {}
        self.latest = 0
        self.max = []
        self.min = []

    def update(self, timestamp: int, price: int) -> None:
        self.records[timestamp] = price 
        self.latest = max(self.latest, timestamp)
        heappush(self.max, [-price, timestamp])
        heappush(self.min, [price, timestamp])

    def current(self) -> int:
        return self.records[self.latest]

        
    def maximum(self) -> int:
        price, time = heappop(self.max)
        while -price != self.records[time]:
            price, time = heappop(self.max)
        heappush(self.max, [price, time])
        return -price
        

    def minimum(self) -> int:
        price, time = heappop(self.min)
        while price != self.records[time]:
            price, time = heappop(self.min)
        heappush(self.min, [price, time])
        return price 

        
       
    
    
    
   


    
        
        

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()




# https://leetcode.com/problems/stock-price-fluctuation/discuss/1514631/Python-SortedList-and-2-heaps-solutions


# class StockPrice:

#     def __init__(self):
#         # record all price & timestamp 
#         self.records = {}
#         # record latest timestamp
#         self.latest = 0
#         self.min_heap = []
#         self.max_heap = []
        

#     def update(self, timestamp: int, price: int) -> None:
#         self.records[timestamp] = price
#         self.latest = max(self.latest, timestamp)
#         # don't remove the old price from the heap, leave it for max & min methods 
#         heapq.heappush(self.min_heap, [price, timestamp])
#         heapq.heappush(self.max_heap, [-price, timestamp])
        
#     def current(self) -> int:
#         return self.records[self.latest]
        
#     # time complexity: O(logN)   
#     def maximum(self) -> int:
#         price, time = heapq.heappop(self.max_heap)
        
#         # if the price doesn't match the records[time], the price has been updated
#         # max_heap stores -price while records stores price 
#         while -price != self.records[time]:
#             # pop pop outdated price & time until price matches the current records[time]
#             price, time = heapq.heappop(self.max_heap)
#         # the last price & time are valid (not outdated) so need to push it back to the heap 
#         heapq.heappush(self.max_heap, [price, time])
        
#         return -price 
        

#     def minimum(self) -> int:
#         price, time = heapq.heappop(self.min_heap)
        
#         while price != self.records[time]:
#             price, time = heapq.heappop(self.min_heap)
        
#         heapq.heappush(self.min_heap, [price, time])
#         return price 
        
        
