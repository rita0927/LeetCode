class DoubleLinkedList:
    
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = DoubleLinkedList(homepage)


    def visit(self, url: str) -> None:
        node = DoubleLinkedList(url)
        node.prev = self.history
        self.history.next = node
        self.history = node 

    def back(self, steps: int) -> str:
        
        while steps >0 and self.history.prev:
            steps -= 1
            self.history = self.history.prev 
        
        return self.history.val 
        

    def forward(self, steps: int) -> str:
        
        while steps > 0 and self.history.next:
            steps -= 1
            self.history = self.history.next 
        
        return self.history.val 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)



# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.history = [homepage]
#         self.cur = 0
        
        
#     def visit(self, url: str) -> None:
#         while self.cur < len(self.history) - 1:
#             self.history.pop()
#         self.history.append(url)
#         self.cur += 1

#     def back(self, steps: int) -> str:
#         while steps > 0 and self.cur > 0:
#             steps -= 1
#             self.cur -= 1
        
#         return self.history[self.cur]
            


#     def forward(self, steps: int) -> str:
#         while steps > 0 and self.cur < len(self.history) - 1:
#             steps -= 1
#             self.cur += 1
#         return self.history[self.cur]
    




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
        