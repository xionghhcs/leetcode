
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        pre = head
        cur = head.next
        hash_table = dict()
        hash_table[pre.val] = 1
        while cur is not None:
            if cur.val in hash_table:
                pre.next = cur.next
                cur = cur.next
            else:
                hash_table[cur.val] = 1
                pre = cur
                cur = cur.next
        return head

        