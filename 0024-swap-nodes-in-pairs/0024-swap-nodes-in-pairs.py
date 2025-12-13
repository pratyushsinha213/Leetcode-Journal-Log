# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        for i in range(0, len(arr)-1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]

        dummy = ListNode()
        curr = dummy

        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next