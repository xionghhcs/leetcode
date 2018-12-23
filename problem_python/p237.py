# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node_next = node.next
        while node_next.next is not None:
            node.val = node.next.val
            node =  node.next
            node_next = node.next
        node.val = node_next.val
        node.next = None