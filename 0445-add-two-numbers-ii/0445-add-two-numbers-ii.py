# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = [], []
        while l1:
            n1.append(str(l1.val))
            l1 = l1.next
        while l2:
            n2.append(str(l2.val))
            l2 = l2.next
        
        num1, num2 = int(''.join(n1)), int(''.join(n2))
        result = str(num1 + num2)
        arr = [int(num) for num in result]

        dummy = ListNode()
        curr = dummy

        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next