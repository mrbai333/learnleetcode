# Date : 06/26/19
# 1.分别对行/列/九宫格分别进行判断，有重复数则返回False
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidCell(board)
    def isValidRow(self,board):
        n = len(board)
        for r in range(n):
            row = [x for x in board[r] if x != '.']
            if len(set(row)) != len(row):
                return False
        return True
    def isValidCol(self,board):
        n = len(board)
        for c in range(n):
            col = [board[r][c] for r in range(n) if board[r][c] != '.']
            if len(set(col)) != len(col):
                return False
        return True
    def isValidCell(self,board):
        n = len(board)
        for r in range(0,n,3):
            for c in range(0,n,3):
                cell = []
                for i in range(3):
                    for j in range(3):
                        num = board[r+i][c+j]
                        if num != '.':
                            cell.append(num)
                if len(set(cell)) != len(cell):
                    return False
        return True