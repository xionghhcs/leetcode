# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        hash_table = dict()
        for i in G:
            hash_table[i] = 1
        ans = 0
        while head:
            if head.val in hash_table:
                ans += 1
                while head and head.val in hash_table:
                    head = head.next
            else:
                head = head.next
        return ans
    