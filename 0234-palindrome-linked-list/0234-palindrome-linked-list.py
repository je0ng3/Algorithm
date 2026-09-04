# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        rev = None
        while slow:
            rev = ListNode(slow.val, rev)
            slow = slow.next
        
        left = head
        while rev:
            if left.val != rev.val:
                return False
            left = left.next
            rev = rev.next
        return True