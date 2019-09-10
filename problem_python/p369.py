# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        stack = []
        cur = head
        while cur is not None:
            stack.append(cur)
            cur = cur.next
        carry = 0
        flag = True
        while len(stack) > 0:
            n = stack.pop()
            tmp = 0
            if flag:
                tmp = n.val + carry + 1
                flag = False
            else:
                tmp = n.val + carry
            n.val = tmp % 10
            carry = tmp // 10
        if carry != 0:
            node = ListNode(carry)
            node.next = head
            return node
        return head
