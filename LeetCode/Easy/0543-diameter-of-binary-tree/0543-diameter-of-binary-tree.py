# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we need left/right/left+right subtrees
        self.maxDiam = 0
        def height(node: Optional[TreeNode]):
            if not node: 
                return 0

            left = height(node.left)
            right = height(node.right)
            self.maxDiam = max(left + right, self.maxDiam)
            return 1+max(left, right)

        height(root)
        return self.maxDiam

            

