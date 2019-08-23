# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        def recur(node, pre):
            if node:
                tmp = node.next
                node.next = pre
                if tmp:
                    pre.next = recur(tmp.next, tmp)
                else:
                    pre.next = None
                return node
            return pre
        return recur(head.next, head)
