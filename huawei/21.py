# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        new_head = ListNode(0)
        rear = new_head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                rear.next = l1
                l1 = l1.next
                rear = rear.next
                rear.next = None
            else:
                rear.next = l2
                l2 = l2.next
                rear = rear.next
                rear.next = None
        
        if l1 is not None:
            rear.next = l1
        if l2 is not None:
            rear.next = l2
        return new_head.next
    