# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node: 'ListNode') -> None:
        if not node or not node.next:
            return  # Edge case: last node can't be deleted this way

        node.val = node.next.val  # Copy next node's value
        node.next = node.next.next  # Skip the next node, effectively deleting it