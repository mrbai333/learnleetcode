# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Date : 06/24/19
# 使用递归的方式进行判断
# 1.判断当前结点是否为空，为空则返回空
# 2.判断当前结点是否等于q或者p，如果等于则返回root
# 3.判断左子树和右子树是否为空，若左右都不为空，则当前root为所求结点，若其中一个为空则返回另一边为答案
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left != None and right != None:return root
        if left == None:
            return right
        else:
            return left