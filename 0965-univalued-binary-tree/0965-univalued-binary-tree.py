# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        unique = set()
        def traverse(node):
            if not node:
                return 
                
            unique.add(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return len(list(unique)) == 1