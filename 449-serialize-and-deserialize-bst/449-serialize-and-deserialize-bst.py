# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:

        self.lst = []
        def dfs(node):
            if not node: return None 
            self.lst.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(self.lst)
                    

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data: return None 
        vals = [int(val) for val in data.split(",")]
        
        def dfs(max_val):
            if not vals: return None
            if vals[0] >= max_val: return None
            
            val = vals.pop(0)
            node = TreeNode(val)
            node.left = dfs(val)
            node.right = dfs(max_val)
            return node
        return dfs(float('inf'))

#         def dfs(lst, min_val, max_val):
#             if not lst: return None 
#             if not min_val < lst[0] < max_val: return None 
            
#             val = lst.pop(0)
#             node = TreeNode(val)
            
#             node.left = dfs(lst, min_val, val)
#             node.right = dfs(lst, val, max_val)
#             return node
        
#         return dfs(vals, float('-inf'), float('inf'))
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#     def serialize(self, root: Optional[TreeNode]) -> str:
#         """Encodes a tree to a single string.
#         """
#         if root:
#             return f"{root.val} {self.serialize(root.left)} {self.serialize(root.right)}" 
#         else:
#             return 'N'
            

#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         """Decodes your encoded data to tree.
#         """
#         vals = data.split()
#         self.i = 0
        
#         def dfs():
#             if vals[self.i] == 'N':
#                 self.i +=1
#                 return None
#             node = TreeNode(int(vals[self.i]))
#             self.i +=1
#             node.left = dfs()
#             node.right = dfs()
#             return node 
            
#         return dfs()
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans