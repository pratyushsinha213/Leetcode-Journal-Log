# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        counter = Counter(arr)
        result = []
        for num, count in counter.items():
            if count == 1:
                result.append(num)
        
        sorted_arr = sorted(result)

        dummy = ListNode()
        curr = dummy

        for val in sorted_arr:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next