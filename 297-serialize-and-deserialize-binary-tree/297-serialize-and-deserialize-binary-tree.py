# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        queue = deque([root])
        res = []
        
        while queue:
            node = queue.popleft()
            if not node:
                res.append('N')
                continue
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        
        return ' '.join(res)
        
        

    def deserialize(self, data):
        
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split()
        if vals[0] == 'N':
            return None
        root = TreeNode(int(vals.pop(0)))
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            left = vals.pop(0)
            right = vals.pop(0)
            node.left = None if left == 'N' else TreeNode(int(left))
            node.right = None if right == 'N' else TreeNode(int(right))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root 
            
           
            
            


















# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         # if not root:
#         #     return 'N'
#         # else:
#         #     return f'{root.val} {self.serialize(root.left)} {self.serialize(root.right)}'

#         stack = [root]
#         res = []
        
#         while stack:
#             node = stack.pop()
#             if not node:
#                 res.append('N')
#                 continue 
#             res.append(str(node.val))
#             stack.append(node.right)
#             stack.append(node.left)
#         return ' '.join(res) 
    

#     def deserialize(self, data):
        
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
        
#         data = data.split()
        
#         def dfs():
#             val = data.pop(0)
#             if val == 'N':
#                 return None
#             node = TreeNode(int(val))
#             node.left = dfs()
#             node.right = dfs()
#             return node 
        
#         return dfs()
            

        





















# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         # if not root:
#         #     return 'N'
#         # else:
#         #     return f'{root.val} {self.serialize(root.left)} {self.serialize(root.right)}'

#         stack = [root]
#         res = []
        
#         while stack:
#             node = stack.pop()
#             if not node:
#                 res.append('N')
#                 continue 
#             res.append(str(node.val))
#             stack.append(node.right)
#             stack.append(node.left)
#         return ' '.join(res) 
    

#     def deserialize(self, data):
        
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
        
#         data = data.split()
        
#         def dfs():
#             val = data.pop(0)
#             if val == 'N':
#                 return None
#             node = TreeNode(int(val))
#             node.left = dfs()
#             node.right = dfs()
#             return node 
        
#         return dfs()
            

        
                            
            
                
            

        
        
        
        
        
        
        
        
        
        
        
        
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))




























#     def serialize(self, root):
#         """Encodes a tree to a single string.

#         :type root: TreeNode
#         :rtype: str
#         """
#         if root:
#             return f"{root.val} {self.serialize(root.left)} {self.serialize(root.right)}"
#         else:
#             return "N"
    


#     def deserialize(self, data):
#         """Decodes your encoded data to tree.

#         :type data: str
#         :rtype: TreeNode
#         """
#         vals = data.split()
#         self.i = 0
        
#         def dfs():
#             if vals[self.i] == "N":
#                 self.i+=1
#                 return None
#             node = TreeNode(int(vals[self.i]))
#             self.i +=1
#             node.left = dfs()
#             node.right = dfs()
#             return node
        
#         return dfs()
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#     def serialize(self, root):
#         """Encodes a tree to a single string.

#         :type root: TreeNode
#         :rtype: str
#         """
#         res = []

#         def dfs(node):
#           if not node:
#             res.append('N')
#             return
#           res.append(str(node.val))
#           dfs(node.left)
#           dfs(node.right)

#         dfs(root)
#         return ','.join(res)



#     def deserialize(self, data):
#         """Decodes your encoded data to tree.

#         :type data: str
#         :rtype: TreeNode
#         """

#         vals = data.split(',')
#         self.i = 0

#         def dfs():
#           if vals[self.i] == 'N':
#             self.i +=1
#             return None
#           node = TreeNode(int(vals[self.i]))
#           self.i +=1
#           node.left = dfs()
#           node.right = dfs()
#           return node
#         return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))