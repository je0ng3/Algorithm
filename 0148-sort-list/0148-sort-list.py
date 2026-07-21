# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeList(self, l1, l2):
        if l1 and l2:
            if l1.val>l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeList(l1.next, l2)
        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 3. 나눌 수 없으면 재귀 끝
        if not head or not head.next:
            return head
        # 1. 중심 찾아서 반으로 나누기
        half = None
        slow = fast = head
        while fast and fast.next:
            half = slow
            slow = slow.next
            fast = fast.next.next
        half.next = None
        # 2. 나눌 수 없을때까지 반복
        l1 = self.sortList(head) # half로 인해 반 나뉜 연결 리스트
        l2 = self.sortList(slow) # half 이후의 연결 리스트
        # 4. 정렬해서 합침
        return self.mergeList(l1, l2)