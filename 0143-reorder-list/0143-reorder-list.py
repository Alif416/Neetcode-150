class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split and reverse second half
        curr = slow.next
        slow.next = None
        pre = None
        while curr:
            t = curr.next
            curr.next = pre
            pre, curr = curr, t

        # merge
        curr = head
        while pre:
            t1, t2 = curr.next, pre.next
            curr.next = pre
            pre.next = t1
            curr, pre = t1, t2