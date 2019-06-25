# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Date : 06/25/19
# 使用广度优先算法进行遍历
# 1.首先从根节点开始判断，如果根节点为空，则返回0，如果不为空，则进行递归判断
# 2.然后对root的左右子节点分别进行递归判断判断，然后取最小值
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: return 1 + self.minDepth(root.right)
        if not root.right: return 1 + self.minDepth(root.left)
        leftminDepth = self.minDepth(root.left)
        rightminDepth = self.minDepth(root.right)
        return 1 + min(leftminDepth,rightminDepth)