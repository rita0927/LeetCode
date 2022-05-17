"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Dictionary which holds old nodes as keys and new nodes as its values
        
        if not head:
            return None
        
        dic = {}
        
        node = head
        
        while node:
            dic[node] = Node(node.val)
            node = node.next
        
        node = head
        
        while node:
            dic[node].next = dic[node.next] if node.next else None
            dic[node].random = dic[node.random] if node.random else None
            node = node.next
        
        return dic[head]
        
        
        
        
        
        