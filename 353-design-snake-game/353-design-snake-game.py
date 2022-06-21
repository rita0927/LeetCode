class SnakeGame:


    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.snake = [[0,0]]
        self.r = 0
        self.c = 0
        self.score = 0
        self.food = food 
        self.dir = {'R': [0,1], 'L': [0,-1], 'U': [-1,0], 'D': [1,0]}
        

    def move(self, direction: str) -> int:
        
        self.r += self.dir[direction][0]
        self.c += self.dir[direction][1]
        
        if self.r < 0 or self.r >= self.height or self.c < 0 or self.c >= self.width:
            return -1
        
        if [self.r,self.c] in self.snake and [self.r, self.c] != self.snake[0]:
            return -1
        self.snake.append([self.r, self.c])
        
        if self.food and [self.r, self.c] == self.food[0]:
            self.food.pop(0)
            self.score += 1
        else:
            self.snake.pop(0)
        
        return self.score 
            
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)



# # use set to check if the snake is going to bite the body
# # set is optional, improve the time complexity at the cost of the space complexity


#     def __init__(self, width: int, height: int, food: List[List[int]]):
#         self.snake = deque([(0,0)])

#         self.snake_set = set([(0,0)])
#         self.m = height
#         self.n = width
#         self.r = 0
#         self.c = 0
#         self.food = food
#         self.score = 0

#     def move(self, direction: str) -> int:
        
#         if direction == 'R':
#             self.c += 1
#         elif direction == 'L':
#             self.c -= 1
#         elif direction == 'U':
#             self.r -= 1
#         elif direction == 'D':
#             self.r += 1
        
#         if self.r < 0 or self.r >= self.m or self.c < 0 or self.c >= self.n:
#             return -1
#         # check if the snake is going to a cell that's occupied by the body already
#         # it's ok the snake is into a cell ocupied by the tail since the tail is leaving that cell once the snake is entering
#         if (self.r,self.c) in self.snake_set and (self.r, self.c) != self.snake[0]:
#             return -1
        
#         if len(self.snake) != len(self.snake_set):
#             print(self.snake, self.snake_set)
        
#         # if the new head cell contains food, need to pop it out from the left of the food 
#         # the tail doesn't move 
#         if self.food and self.food[0] == [self.r, self.c]:
#             self.food.pop(0)
#             self.score += 1
#         else:
#             # the tail pops out only if the new head cell doesn't contain the food 
#             # previous tail needs to be popped out (tail moves to the next position)
#             tail = self.snake.popleft()
#             self.snake_set.remove(tail)
#         # need to remove the tail (if it's needed) before adding the new head 
#         # if the tail occupies the new head cell, add before remove from set will cause error in snake set 
            
#         # append the new head cell to the snake
#         self.snake.append((self.r, self.c))
#         self.snake_set.add((self.r, self.c))
#         return self.score
        
        










#     # O(m*n) to iterate the snake and see if it bites itself
#     # O(m*n+l) where l is the number of food items. m*n for the snake structure, l for the food structure 

#     def __init__(self, width: int, height: int, food: List[List[int]]):
#         self.m = height
#         self.n = width
#         self.snake = [[0,0]]
#         self.food = food
#         self.r = 0
#         self.c = 0
#         self.score = 0
        

#     def move(self, direction: str) -> int:
#         if direction == 'L':
#             self.c -= 1
#         elif direction == 'R':
#             self.c += 1
#         elif direction == 'U':
#             self.r -= 1
#         elif direction == 'D':
#             self.r += 1
        
#         if self.r < 0 or self.r >= self.m or self.c < 0 or self.c >= self.n:
#             return -1
        
#         if [self.r, self.c] in self.snake and [self.r,self.c] != self.snake[0]:
#             return -1


#         self.snake.append([self.r, self.c])

#         if self.food and [self.r, self.c] == self.food[0]:
#             self.food.pop(0)
#             self.score += 1
#         else:
#             tail = self.snake.pop(0)
#         return self.score 
        