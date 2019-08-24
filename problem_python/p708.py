"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if head is None:
            node.next = node
            return node
        cur = head
        while cur.next != head:
            if cur.val <= insertVal and insertVal <= cur.next.val:
                break
            if cur.val > cur.next.val and cur.val <= insertVal and cur.next.val <= insertVal:
                break
            if cur.val > cur.next.val and cur.val >= insertVal and cur.next.val >= insertVal:
                break
            cur = cur.next
        
        n = cur.next
        cur.next = node
        node.next = n
        return head
    