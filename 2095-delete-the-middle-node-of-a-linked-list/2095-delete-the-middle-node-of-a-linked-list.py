class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        # Step 1: get length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Step 2: find node before middle
        middle = length // 2
        curr = head
        for _ in range(middle - 1):
            curr = curr.next

        # Step 3: delete middle
        curr.next = curr.next.next

        return head