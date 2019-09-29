class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_table = dict()
        dist_table = dict()
        for idx, v in enumerate(nums):
            if v in hash_table:
                dist = idx - hash_table[v]
                if v in dist_table and dist_table[v] > dist:
                    dist_table[v] = dist
                    if dist <= k:
                        return True
                else:
                    dist_table[v] = dist

                hash_table[v] = idx
            else:
                hash_table[v] = idx
        return False

class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = dict()
        ans = 0
        for i, v in enumerate(nums):
            if v not in table:
                table[v] = i
            else:
                if i - table[v] <= k:
                    return True
                table[v] = i
        return False
