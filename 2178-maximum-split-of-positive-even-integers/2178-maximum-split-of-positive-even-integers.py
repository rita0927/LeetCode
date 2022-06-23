class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        res = []
        
        if finalSum % 2 or finalSum < 2:
            return []
        
        cur_sum = 0
        cur_num = 2

        while cur_sum < finalSum:
            res.append(cur_num)
            cur_sum += cur_num
            cur_num +=2
        
        if cur_sum == finalSum:
            return res 
        else:
            # res.remove(cur_sum - finalSum)
            res.pop((cur_sum-finalSum)//2 -1)
        
        return res 
        