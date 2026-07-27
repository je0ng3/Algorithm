# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = float('inf')
        prev = -float('inf') # node의 부모노드
        def inorder(node):
            nonlocal result, prev
            if node.left:
                inorder(node.left)
            result = min(result, node.val-prev)
            prev = node.val
            if node.right:
                inorder(node.right)
        inorder(root)
        return result
