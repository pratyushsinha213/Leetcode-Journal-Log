# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def traverse(node, arr):
            if not node:
                return
            arr.append(node.val)
            traverse(node.left, arr)
            traverse(node.right, arr)

        traverse(root, arr)
        return arr