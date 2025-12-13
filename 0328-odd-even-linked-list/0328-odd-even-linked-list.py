# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        odd, even = [arr[i] for i in range(len(arr)) if i % 2 == 0], [arr[i] for i in range(len(arr)) if i % 2 == 1]

        merged = odd + even

        dummy = ListNode()
        curr = dummy

        for val in merged:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next