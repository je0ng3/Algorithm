# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(None)
        even = ListNode(None)
        o, e = odd, even
        while head and head.next:
            odd.next = head
            even.next = head.next
            odd, even = odd.next, even.next
            head = head.next.next
        if head:
            odd.next = head
            odd = odd.next
        even.next = None
        odd.next = e.next
        return o.next