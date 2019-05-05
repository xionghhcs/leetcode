# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        head = new_head
        rear = new_head
        for _ in range(n + 1):
            rear = rear.next
        while rear != None:
            rear = rear.next
            head = head.next
        head.next = head.next.next
        return new_head.next
        