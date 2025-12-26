class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def search(node):
            if not node:
                return None
            
            if node.val == val:
                return node
            elif val < node.val:
                return search(node.left)
            else:
                return search(node.right)

        return search(root)