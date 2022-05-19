class TicTacToe:

    def __init__(self, n: int):
        self.r = [0] * n
        self.c = [0] * n
        self.dia = 0
        self.anti = 0
        
      

    def move(self, row: int, col: int, player: int) -> int:
        n = len(self.r)
        cur = 1 if player == 1 else -1
        
        self.r[row] += cur
        self.c[col] += cur
        
        if row == col:
            self.dia += cur
        
        if col == n - row - 1:
            self.anti += cur
            
        if abs(self.r[row]) == n or abs(self.c[col]) == n or abs(self.dia) == n or abs(self.anti) == n:
            return player
        return 0
        
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
















#     def __init__(self, n: int):
#         self.rows = [0] * n
#         self.cols = [0] * n
#         self.diagonal = 0
#         self.antiDiagonal = 0
        

#     def move(self, row: int, col: int, player: int) -> int:
#         n = len(self.rows)
#         cur = 1 if player == 1 else -1
#         self.rows[row] += cur
#         self.cols[col] += cur
        
#         if row == col:
#             self.diagonal += cur
        
#         if col == (n-row-1):
#             self.antiDiagonal += cur
        
#         if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diagonal) == n or abs(self.antiDiagonal) == n:
#             return player
#         return 0