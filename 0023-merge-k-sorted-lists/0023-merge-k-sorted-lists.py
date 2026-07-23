# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwo(self, l1, l2):
        if l1 and l2:
            if l1.val>l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwo(l1.next, l2)
            return l1
        return l1 or l2

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        l1 = lists[0]
        for l2 in lists[1:]:
            l1 = self.mergeTwo(l1, l2)
        return l1