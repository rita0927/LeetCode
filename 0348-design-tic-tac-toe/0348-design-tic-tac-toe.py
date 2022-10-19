class TicTacToe:

    def __init__(self, n: int):
        self.rows=[0]*n
        self.cols=[0]*n
        self.diagonal=0
        self.antiDiagonal=0
        

      

    def move(self, row: int, col: int, player: int) -> int:
        n=len(self.rows)
        cur=1 if player==1 else -1
        self.rows[row]+=cur
        self.cols[col]+=cur

        if row==col:
            self.diagonal+=cur
        if row==(n-col-1):
            self.antiDiagonal+=cur

        if abs(self.rows[row])==n or abs(self.cols[col])==n or abs(self.diagonal)==n or abs(self.antiDiagonal)==n:
            return player
        return 0
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)














# O(1), O(n)

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