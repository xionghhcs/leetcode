# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(0)
        rear = new_head
        carry = 0
        ans = 0
        b = 0
        while l1 is not None and l2 is not None:
            tmp = l1.val + l2.val + carry
            carry = tmp // 10
            rear.next = ListNode(tmp % 10)
            rear = rear.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            tmp = l1.val + carry
            carry = tmp // 10
            rear.next = ListNode(tmp % 10)
            rear = rear.next
            l1 = l1.next
        while l2 is not None:
            tmp = l2.val + carry
            carry = tmp // 10
            rear.next = ListNode(tmp % 10)
            rear = rear.next
            l2 = l2.next
        if carry!= 0:
            rear.next = ListNode(carry)
            
        return new_head.next
