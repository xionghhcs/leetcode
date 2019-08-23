# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        total_num = 0
        tmp = head
        while tmp is not None:
            total_num += 1
            tmp = tmp.next
        idx = total_num // 2
        while idx > 0:
                head = head.next
                idx -= 1
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        def dfs(root, cnt):
            if root:
                dfs(root.next, cnt + 1)
                if cnt == self.ans:
                    self.res = root
            else:
                self.ans = cnt // 2
        dfs(head, 0)
        return self.res
    