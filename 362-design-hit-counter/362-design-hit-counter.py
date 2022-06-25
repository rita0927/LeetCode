class HitCounter:

    # space: O(N) in the case of repetitions in the same timestamp, the space required for storing those values O(1)
    def __init__(self):
        self.queue = deque()
        self.count = 0

    def hit(self, timestamp: int) -> None:
        if self.queue and timestamp == self.queue[-1][0]:
            self.queue[-1][1] += 1
        else:
            self.queue.append([timestamp, 1])
        self.count+=1
        
    # time: O(N) 
    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0][0] <= timestamp - 300:
            t,c = self.queue.popleft()
            self.count -= c
        return self.count 
            

            

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)