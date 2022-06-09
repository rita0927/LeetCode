class DoubleLinkedList:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = DoubleLinkedList(homepage)
        
    def visit(self, url: str) -> None:
        node = DoubleLinkedList(url)
        node.prev = self.cur
        self.cur.next= node
        self.cur = self.cur.next 
        

    def back(self, steps: int) -> str:
        while steps and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val 
        

    def forward(self, steps: int) -> str:
        while steps and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val 
       
    
    
    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)




# class DoubleLinkedList:
#     def __init__(self, val):
#         self.val = val
#         self.prev = None
#         self.next = None 



# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.node = DoubleLinkedList(homepage)
        
#     def visit(self, url: str) -> None:
#         new_node = DoubleLinkedList(url)
#         new_node.prev = self.node
#         self.node.next = new_node
#         self.node = self.node.next 
        

#     def back(self, steps: int) -> str:
        
#         while steps and self.node.prev:
#             self.node = self.node.prev
#             steps-= 1
        
#         return self.node.val
        

#     def forward(self, steps: int) -> str:
        
#         while steps and self.node.next:
#             self.node = self.node.next
#             steps -= 1
        
#         return self.node.val 
        