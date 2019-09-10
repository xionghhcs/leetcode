# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        l = 0
        cursor = root
        while cursor:
            l += 1
            cursor = cursor.next
        
        group_len = l // k
        group_rear = l % k
        
        ans = []
        
        cur = root
        while cur:
            ans.append(cur)
            cnt = 1
            while cnt < group_len and cur:
                cur = cur.next
                cnt += 1
            if group_len > 0 and group_rear > 0 and cur:
                cur = cur.next
                group_rear -= 1
            if cur:
                cur_next = cur.next
                cur.next = None
                cur = cur_next
                
        while len(ans) < k:
            ans.append(None)

        return ans
    