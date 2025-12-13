class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        n = len(arr)
        k %= n

        if k == 0:
            return head

        # Rotate array
        arr = arr[-k:] + arr[:-k]

        # Rebuild linked list
        dummy = ListNode()
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next