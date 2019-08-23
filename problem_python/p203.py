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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newHead = ListNode(0)
        newHead.next = head
        
        def recur(node, pre):
            if node:
                if pre:
                    if val == node.val:
                        pre.next = node.next
                        recur(node.next, pre)
                        node.next=None
                    else:
                        recur(node.next, node)
                else:
                    pre = node
                    recur(node.next, pre)
        recur(head, newHead)
        return newHead.next
    