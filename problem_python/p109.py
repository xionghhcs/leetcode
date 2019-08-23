# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head  is None:
            return None
        pre = None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        if pre is not None:
            pre.next = None
        if head == slow:
            return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
    