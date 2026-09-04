# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            slow, rev, rev.next = slow.next, slow, rev
        
        if fast:
            slow = slow.next
        
        while rev and rev.val==slow.val:
            slow, rev = slow.next, rev.next
        
        return not rev