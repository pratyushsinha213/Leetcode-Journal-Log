# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def traverse(node, arr):
            if not node:
                return
            traverse(node.left, arr)
            traverse(node.right, arr)
            arr.append(node.val)

        traverse(root, arr)
        return arr