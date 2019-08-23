# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(tmp)
        newHead = ListNode(0)
        rear = newHead
        while l and r:
            if l.val < r.val:
                tmp = l.next
                l.next = None
                rear.next = l
                l = tmp
            else:
                tmp = r.next
                r.next = None
                rear.next = r
                r = tmp
            rear = rear.next
        rear.next = l if l else r
        return newHead.next
