# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s = set()
        def explore(node):
            if not node:
                return
            s.add(node.val)
            explore(node.left)
            explore(node.right)
        
        explore(root)
        a = sorted(list(s))
        print(a)
        return a[1] if len(a) > 1 else -1