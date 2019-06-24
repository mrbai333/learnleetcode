# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Date : 06/24/19
# 使用递归的方式进行判断
# 1.递归使用valid函数进行递归调用
# 2.设置最大值和最小值，初始值为正无穷和负无穷
# 3.valid函数首先进行空集判断，如果为空集则返回True
# 4.然后判断root的值是否比最大值大或者比最小值小，如果比最大值大或比最小值小，则返回False
# 5.因为按照定义root的值应该比左子树的值大比右子树的值小
# 6.最后按照递归分别对root的左右子树分别进行判断，判断时，左子树的最大值被赋为root的值，而右子树的最小值被赋为root的值
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid(root,float('-inf'),float('inf'))
    def valid(self,root,min,max):
        if not root:return True
        if max <= root.val or min >= root.val:
            return False
        else:
            return self.valid(root.left,min,root.val) and self.valid(root.right,root.val,max)
        