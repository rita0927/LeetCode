class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.m = height
        self.n = width
        self.snake = [[0,0]]
        self.food = food
        self.r = 0
        self.c = 0
        self.score = 0
        

    def move(self, direction: str) -> int:
        if direction == 'L':
            self.c -= 1
        elif direction == 'R':
            self.c += 1
        elif direction == 'U':
            self.r -= 1
        elif direction == 'D':
            self.r += 1
        
        if self.r < 0 or self.r >= self.m or self.c < 0 or self.c >= self.n:
            return -1
        
        if (self.r, self.c) in self.snake and (self.r,self.c) != self.snake[0]:
            return -1

        self.snake.append((self.r, self.c))
        if self.food and [self.r, self.c] == self.food[0]:
            self.food.pop(0)
            self.score += 1
        else:
            self.snake.pop(0)
        return self.score 
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)