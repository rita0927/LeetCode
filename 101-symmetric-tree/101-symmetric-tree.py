# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        queue =deque([root.left, root.right])
        
        while queue:
            
            node1 = queue.popleft()
            node2 = queue.popleft()
            
            if not node1 and not node2:
                continue
            if node1 and node2 and node1.val == node2.val:
                queue.append(node1.left)
                queue.append(node2.right)
                queue.append(node1.right)
                queue.append(node2.left)
            else:
                return False
        return True
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack = [root.left, root.right]
        
#         while stack:
#             node1 = stack.pop()
#             node2 = stack.pop()
            
#             if not node1 and not node2:
#                 continue
#             if not node1 or not node2 or node1.val != node2.val:
#                 return False
#             stack.append(node1.left)
#             stack.append(node2.right)
#             stack.append(node1.right)
#             stack.append(node2.left)
#         return True

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def isMirror(left, right):
#             if not left and not right:
#                 return True
#             if not left or not right:
#                 return False
            
#             return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
#         return isMirror(root.left, root.right)
        
        
        
        
        
        
        
#         def dfs(left, right):
#             if not left and not right:
#                 return True    
#             if not left or not right:
#                 return False
#             return left.val == right.val and dfs(left.left, right.right) and dfs (left.right, right.left)
            
#         return dfs(root.left, root.right)
            
            
            
            
        