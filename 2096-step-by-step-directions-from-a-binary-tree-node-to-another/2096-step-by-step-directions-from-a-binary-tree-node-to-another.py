# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parents = {}
        self.start = None

        def findNode(parent, node):

            parents[node] = parent
            if node.val == startValue:
                self.start = node
            
            if node.left:
                findNode(node, node.left)
            if node.right:
                findNode(node, node.right)
            
        findNode(None, root)
        queue = deque([(self.start, '')])
        visited = set()
        # visited.add(self.start.val)
        
        while queue:

            node, path = queue.popleft()
            visited.add(node.val)
            
            if node.val == destValue:
                return path
            if node.left and node.left.val not in visited:
                queue.append((node.left, path+'L'))
                # visited.add(node.left.val)
            if node.right and node.right.val not in visited:
                queue.append((node.right, path+'R'))
                # visited.add(node.right.val)
            if parents[node] and parents[node].val not in visited:
                queue.append((parents[node], path+'U'))
                # visited.add(parents[node].val)
                    
        
                        