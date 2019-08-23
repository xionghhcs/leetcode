# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        newHead1 = ListNode(0)
        newHead2 = ListNode(0)
        r1 = newHead1
        r2 = newHead2
        cur = head
        while cur:
            tmp = cur.next
            cur.next = None
            if cur.val < x:
                r1.next = cur
                r1 = r1.next
            else:
                r2.next = cur
                r2 = r2.next
            cur = tmp
        r1.next = newHead2.next
        return newHead1.next
    