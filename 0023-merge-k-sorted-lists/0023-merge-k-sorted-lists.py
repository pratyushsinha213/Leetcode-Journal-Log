# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = []
        for l in lists:
            while l:
                merged.append(l.val)
                l = l.next
        
        sorted_merged = sorted(merged)

        dummy = ListNode()
        curr = dummy

        for val in sorted_merged:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next