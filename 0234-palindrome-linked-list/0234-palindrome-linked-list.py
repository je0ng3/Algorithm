# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p = []
        node = head
        while node:
            p.append(node.val)
            node = node.next
        
        while len(p)>1:
            if p.pop(0)!=p.pop(-1):
                return False
        return True
        