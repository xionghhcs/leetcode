# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        pre = new_head
        post = pre.next
        while post is not None:
            if post.val == val:
                pre.next = post.next
                post = pre.next
            else:
                pre = post
                post = post.next
        return new_head.next