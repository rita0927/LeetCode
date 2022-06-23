class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.arr = []


    def add(self, point: List[int]) -> None:
        # count the freq of each coordinate
        self.points[tuple(point)] += 1
        self.arr.append(point)


    def count(self, point: List[int]) -> int:
        count = 0
        x,y = point
        for x1,y1 in self.arr:
            # must have positive area (can't be identical coordinates)
            if abs(x1-x) == abs(y1-y) and x1 != x and y1 != y:
                # if (x1,y) in self.points and (x,y1) in self.points:
                #     count += self.points[(x1,y)] * self.points[(x,y1)]
                
                # if either point doesn't exist, the count won't increase
                count += self.points[(x,y1)] * self.points[(x1,y)]
        return count 
                
            
        

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)