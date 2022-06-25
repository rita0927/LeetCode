class Solution:

    def __init__(self, w: List[int]):
        # create a range based on the sum of all the w[i]
        # each index is represented by a segment of the range 
        # pick a random num from the range, and find the corresponding index/segment
        
        # append the prefix (segment cut off point)
        self.prefix = []
        prefix = 0
        for i in w:
            prefix += i
            self.prefix.append(prefix)
        self.total = prefix
        
    def pickIndex(self) -> int:
        
        # pick a random num from the range of self.total 
        # use random.random so that the range is [0,total), doesn't include the total number in the range 
        num = self.total * random.random()
        l = -1 
        r = len(self.prefix)
        
        while l+1 != r:
            mid = (l+r)//2
            # l is the ending of previous segment
            if self.prefix[mid] <= num:
                l = mid
            # find the segment that contains the num, self.prefix[l] <= num < self.prefix[r]
            else:
                r = mid 
        return r 
        
        


        



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()