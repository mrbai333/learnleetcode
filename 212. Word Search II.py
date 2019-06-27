# Date : 06/27/19
# 1.使用深度优先搜索DFS进行搜索判断，每次便利当前字母的上下左右4个字母
dx = [-1,1,0,0]
dy = [0,0,-1,1]
end_of_word = "#"
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        if not words:
            return []
        self.result = set()
        root = collections.defaultdict()
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch,collections.defaultdict())
            node[end_of_word] = end_of_word
        
        self.m, self.n = len(board), len(board[0])
        
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board,i,j,"",root)
        return self.result
    def _dfs(self,board,i,j,cur_word,cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if end_of_word in cur_dict:
            self.result.add(cur_word)
        tmp,board[i][j] = board[i][j], "@"
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != "@" and board[x][y] in cur_dict:
                self._dfs(board,x,y,cur_word,cur_dict)
        board[i][j] = tmp