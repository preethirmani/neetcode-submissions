# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(root):
            if root is None:
                return 0
            left_max = dfs(root.left)
            right_max = dfs(root.right)

            self.result = max(self.result, left_max + right_max)
            return 1 + max(left_max, right_max)
        dfs(root)
        return self.result
