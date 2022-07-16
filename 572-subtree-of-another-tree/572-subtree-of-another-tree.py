# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False
            return helper(n1.left, n2.left) and helper(n1.right, n2.right)
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                continue 
            if helper(node, subRoot):
                return True
            queue.append(node.left)
            queue.append(node.right)
        return False 
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # Time:O(nm) for each of n nodes there is at max m computations
#         # Space: O(logn+logm) : max would be height of each tree together (recursion & stack)
#         def helper(n1, n2):
#             if not n1 and not n2:
#                 return True
#             if not n1 or not n2 or n1.val != n2.val:
#                 return False
#             return helper(n1.left, n2.left) and helper(n1.right, n2.right)
              
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if helper(node, subRoot):
#                 return True
#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)
   
#         return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def sameTree(n1, n2):
#             if not n1 and not n2:
#                 return True
#             if not n1 or not n2 or n1.val != n2.val:
#                 return False
#             return sameTree(n1.left, n2.left) and sameTree(n1.right, n2.right)
        
#         queue = deque([root])
#         while queue:
#             node = queue.popleft()
#             if sameTree(node, subRoot):
#                 return True
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
        
#         return False 
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def helper(n1, n2):
            
#             if not n1 and not n2:
#                 return True
            
#             if not n1 or not n2 or n1.val != n2.val:
#                 return False
            
#             return helper(n1.left, n2.left) and helper(n1.right, n2.right)
        
#         stack = [root]
#         while stack:
#             n1 = stack.pop()
#             if not n1:
#                 continue
            
#             if helper(n1, subRoot):
#                 return True
            
#             stack.append(n1.left)
#             stack.append(n1.right)
#         return False 
            
        
        
            
            

        


        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
#         def helper(root1, root2):
#             if not root1 and not root2:
#                 return True
#             if not root1 or not root2 or root1.val != root2.val:
#                 return False
#             else:
#                 return helper(root1.left, root2.left) and helper(root1.right, root2.right)
            
        
#         def dfs(node):
#             if node:
#                 if node.val == subRoot.val:
#                     if helper(node, subRoot):
#                         return True
#                 return dfs(node.left) or dfs(node.right)
            
#         return dfs(root)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def convertToString(node):
#             if node:
#                 # use the "#" as a deliminator, example case  [12], [2] 
#                 return f"#{node.val} {convertToString(node.left)} {convertToString(node.right)}"
        
#         return convertToString(subRoot) in convertToString(root)
        
        
        
        
        
        
        
        
        
        
        
        
   
        
#         def dfs(root, subRoot):
            
#             if not root and not subRoot:
#                 return True
#             elif not root or not subRoot or root.val != subRoot.val:
#                 return False
#             else:
#                 return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
        
#         queue = deque([root])
        
#         while queue:
#             node = queue.popleft()
#             if node.val == subRoot.val:
#                 if dfs(node, subRoot):
#                     return True
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         return False 
            
            
        
        

            
                