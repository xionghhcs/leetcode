# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if head.next is None:
            return True
        slow = head
        fast = slow.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail = slow.next
        slow.next = None
        
        tailHead = ListNode(0)
        while tail:
            tmp = tail.next
            tailTmp = tailHead.next
            
            tailHead.next = tail
            tail.next = tailTmp
            
            tail = tmp
        
        tail = tailHead.next
        
        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True
    