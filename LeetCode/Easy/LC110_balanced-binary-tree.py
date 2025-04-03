# LC 110 : https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            left_depth = height(root.left)
            right_depth = height(root.right)
            return max(left_depth, right_depth) + 1

        if not root:
            return True

        if (
            abs(height(root.left) - height(root.right)) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        ):
            return True
        return False
