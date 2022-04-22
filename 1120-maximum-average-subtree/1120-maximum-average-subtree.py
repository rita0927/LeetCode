# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        maxAvg = float("-inf")
        
        def findAvg(node):
            nonlocal maxAvg
            
            if not node:
                return (0, 0)

            total1, num1 = findAvg(node.left)
            total2, num2= findAvg(node.right)
            
            total = total1 + total2 + node.val
            num = num1 + num2 + 1
            
            maxAvg = max(maxAvg, total/num)
            
            
            return (total, num)
        
        findAvg(root)
        
        return maxAvg