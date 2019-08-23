# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp = slow.next
        slow.next = None
        newHead = ListNode(0)
        rear = newHead
        
        # reverse rear part
        rearHead = ListNode(0)
        rear = rearHead
        while tmp:
            n = rearHead.next
            rearHead.next = tmp
            
            tt = tmp.next
            
            tmp.next = n
            
            tmp = tt
        tmp = rearHead.next
        
        while head and tmp:
            rear.next = head
            head = head.next
            rear = rear.next

            rear.next = tmp
            tmp = tmp.next
            rear = rear.next
        if head is not None:
            rear.next = head
            rear = rear.next
        if tmp is not None:
            rear.next = tmp
            rear = rear.next
        return newHead.next
