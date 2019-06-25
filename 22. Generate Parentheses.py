# Date : 06/25/19
# 1.使用递归搜索进行判断
# 2.为了减少搜索次数，仅对符合条件的括号进行生成和添加
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.results = []
        self._gen(0,0,n,'')
        return self.results
    def _gen(self,left,right,n,result):
        if left == n and right == n:
            self.results.append(result)
            return
        if left < n:
            self._gen(left+1,right,n,result+'(')
        if left > right and right < n:
            self._gen(left,right+1,n,result+')')