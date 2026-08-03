# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q = deque([root])
        result = []
        while q:
            level_size = len(q)
            cur_list = []
            for _ in range(level_size):
                cur = q.popleft()
                cur_list.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            result.append(cur_list)

        return result