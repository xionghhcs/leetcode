# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.temp = head
        return self.check(head)
        
    
    def check(self, node):
        if node is None:
            return True
        flag = self.check(node.next) and (self.temp.val == node.val)
        self.temp = self.temp.next
        return flag

class Solution2:
    def isPalindrome(self, head):
        ans = []
        while head is not None:
            ans.append(head.val)
        i = 0
        j = len(ans) - 1
        while i<=j:
            if ans[i] != ans[j]:
                return False
            i += 1
            j -= 1
        return True

class Solution3:
    def isPalindrome(self, head):
        pass


