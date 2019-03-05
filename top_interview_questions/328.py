# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        even_head = ListNode(0)
        even_cur = even_head
        odd_head = ListNode(0)
        odd_cur = odd_head

        cur = head
        while cur is not None:
            tmp = cur
            cur = cur.next
            tmp.next = None
            odd_cur.next = tmp
            odd_cur = odd_cur.next

            if cur is not None:
                tmp = cur
                cur = cur.next
                tmp.next = None
                
                even_cur.next = tmp
                even_cur = even_cur.next
            else:
                break
        odd_cur.next = even_head.next
        return odd_head.next


