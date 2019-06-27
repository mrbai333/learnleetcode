# Date : 06/27/19
# 1.使用深度优先搜索DFS进行搜索判断，每次便利当前字母的上下左右4个字母
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def find(board,word,i,j,m,n):
            if word == "":
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            elif word[0] == board[i][j]:
                board[i][j] = None
                res = find(board,word[1:],i+1,j,m,n) or find(board,word[1:],i-1,j,m,n) or find(board,word[1:],i,j+1,m,n) or find(board,word[1:],i,j-1,m,n)
                board[i][j] = word[0]
                return res
        if not word:
            return []
        if not board or not board[0]:
            return []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if find(board,word,i,j,m,n):
                    return True
        return False