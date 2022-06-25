class HitCounter:

    def __init__(self):
        self.queue = deque()
        

    def hit(self, timestamp: int) -> None:
        if self.queue and timestamp == self.queue[-1][0]:
            self.queue[-1][1] += 1
        else:
            self.queue.append([timestamp, 1])
        

    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0][0] <= timestamp - 300:
            self.queue.popleft()
        
        count = [x[1] for x in self.queue]
        return sum(count)

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)