# Date : 06/24/19
# 使用递归的方式进行判断
# 1.递归使用while函数进行递归判断
# 2.如果root的值大于q和p，令root赋值为root的左子节点
# 3.如果root的值大于q和p，令root赋值为root的右子节点
# 4.如果root的值为q和p的中间值，则root为所求结点
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        return False