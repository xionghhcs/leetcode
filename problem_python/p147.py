# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        newHead = ListNode(0)
        def insert(head, node):
            rear = head
            if rear.next is None:
                rear.next = node
                return 
            else:
                cur = head
                while cur and cur.next:
                    if cur.next.val >= node.val:
                        node.next = cur.next
                        cur.next = node
                        return 
                    cur = cur.next
                cur.next = node
                
        
        cur = head
        while cur:
            tmp = cur.next
            cur.next = None
            insert(newHead, cur)
            cur = tmp
        return newHead.next
    