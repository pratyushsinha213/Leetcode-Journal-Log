# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        result = []
        for num in arr:
            if num == val:
                continue
            else:
                result.append(num)
            
        dummy = ListNode()
        curr = dummy

        for val in result:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next