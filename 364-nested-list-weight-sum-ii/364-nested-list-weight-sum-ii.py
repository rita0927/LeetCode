# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        res = []
        maxDepth = 1
        
        def helper(nested, depth):
            nonlocal maxDepth
            
            maxDepth = max(maxDepth, depth)
            
            for lst in nested:
                
                if lst.isInteger():
                    res.append((lst.getInteger(), depth))
                else:
                    helper(lst.getList(), depth + 1)
                    
        helper(nestedList, 1)
        
        total = 0
        
        for integer, depth in res:
            total +=integer * (maxDepth - depth + 1)
        
        return total 
        
        
        
#         self.total = 0
#         maxDepth = 0
        
#         stack1 = [(nestedList, 1)]
#         while stack1:
#             lst, level = stack1.pop()
            
#             for el in lst:
#                 if el.isInteger(): 
#                     maxDepth = max(maxDepth, level)
#                 else:
#                     stack1.append((el.getList(), level + 1))
                    
#         stack2 = [(nestedList,1)]
#         while stack2:
#             lst, level = stack2.pop()
            
#             for el in lst:
#                 if el.isInteger():
#                     self.total += el.getInteger() * (maxDepth - level + 1)
#                 else:
#                     stack2.append((el.getList(), level + 1))
                        
#         return self.total 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        