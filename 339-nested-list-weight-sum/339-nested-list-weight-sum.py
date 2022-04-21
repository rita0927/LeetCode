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
    def depthSum(self, nestedList: List[NestedInteger], depth = 1) -> int:
        total = 0
        
        for nested in nestedList:
            if nested.isInteger():
                total += nested.getInteger() * depth
            else:
                total += self.depthSum(nested.getList(), depth + 1)
        
        return total
                
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # store List in the stack
#         stack = [(nestedList, 1)]
#         self.total = 0
        
#         while stack:
#             lst, depth = stack.pop()
            
#             # the type of lst is List
#             # the type of el is NestedInteger
#             for el in lst:
                
#                 if el.isInteger():
#                     self.total += el.getInteger() * depth
#                 else:
#                     # store List in the stack
#                     stack.append((el.getList(), depth + 1))
            
#         return self.total 
        
        
        
        
# class Solution:
#     def depthSum(self, nestedList: List[NestedInteger], depth = 1) -> int:
#         total = 0
#         for el in nestedList:
#             if el.isInteger():
#                 total += el.getInteger() * depth 
#             else:
#                 total += self.depthSum(el.getList(), depth + 1)
            
#         return total     
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        