class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        
        l = [1] * n
        stack = [(arr[0], 1)]
        
        for i in range(1, n):
            while stack and arr[i] <= stack[-1][0]:
                l[i] += stack.pop()[1]
            stack.append((arr[i], l[i]))
            
        r = [1] * n
        stack = [(arr[-1], 1)]
        
        for i in range(n-2, -1, -1):
            while stack and arr[i] < stack[-1][0]:
                r[i] += stack.pop()[1]
            stack.append((arr[i], r[i]))
        
        res = 0
        
        for i in range(n):
            res += arr[i] * l[i] * r[i]
        
        return res % (10** 9 + 7)