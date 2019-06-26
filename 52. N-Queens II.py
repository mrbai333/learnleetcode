# Date : 06/26/19
# 使用广度优先算法进行遍历
# 1.分别对行/列/斜线方向进行判断
# 2.要注意判断完后，self.DFS前后的add和remove
# 3.最后只解除答案中的个数
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result = []
        self.cols = set(); self.p = set(); self.q = set()
        self.DFS(n,0,[])
        return self._gen(n)
    def DFS(self,n,row,result):
        if row >= n:
            self.result.append(result)
            return
        for col in range(n):
            if col in self.cols or row + col in self.p or row - col in self.q:
                continue
            self.cols.add(col)
            self.p.add(row + col)
            self.q.add(row - col)
            self.DFS(n,row+1,result+[col])
            self.cols.remove(col)
            self.p.remove(row + col)
            self.q.remove(row - col)
    def _gen(self,n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n-i-1))
        return len([board[i:i+n] for i in range(0,len(board),n)])