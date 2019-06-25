# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Date : 06/25/19
# 使用广度优先算法进行遍历
# 1.首先从根节点开始判断，如果根节点为空，则返回空列表，如果不为空，则加入python的collection.deque类中
# 2.然后对deque进行循环判断，对deque中每一个元素进行弹出操作，并将该元素的值加入当前层级的列表中以及将该元素的子节点加入deque中
# 3.将该层级的列表加入总列表中，进入下一层级的循环，直到该Tree结点都遍历完。
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        result = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(current_level)
        return result