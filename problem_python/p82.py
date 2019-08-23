# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        newHead = ListNode(0)
        newHead.next = head
        rear = newHead
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                tmp = cur
                while tmp and tmp.val == cur.val:
                    tmp = tmp.next
                rear.next = tmp
                cur = tmp
            else:
                rear = rear.next
                cur = cur.next
        return newHead.next
    