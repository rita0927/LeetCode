class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        
        for first, last, inc in bookings:
            res[first - 1] +=inc
            if last < n:
                res[last] -= inc
        
        for i in range(1,n):
            res[i] += res[i-1]
        return res 
        
        