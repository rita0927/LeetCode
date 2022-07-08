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
        if not root:
            return 'N'
        else:
            return f'{root.val} {self.serialize(root.left)} {self.serialize(root.right)}'

        
        
        
        

    def deserialize(self, data):
        
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data = data.split()
        i = -1
        
        def dfs():
            nonlocal i
            i += 1
            if data[i] == 'N':
                return None
            node = TreeNode(int(data[i]))
            node.left = dfs()
            node.right = dfs()
            return node 
        
        return dfs()
            

        
                            
            
                
            

        
        
        
        
        
        
        
        
        
        
        
        
        
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