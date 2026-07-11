# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_dummy=ListNode(0)
        after_dummy=ListNode(0)
        before=before_dummy
        after=after_dummy
    


        curr=head
        while curr:
            next_node=curr.next
            curr.next=None
            if curr.val<x:
                before.next=curr
                before=curr
            elif curr.val>=x:
                after.next=curr
                after=curr
            curr=next_node
        before.next=after_dummy.next
        return before_dummy.next

        