class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_table = dict()
        for i in nums:
            if i in hash_table:
                return True
            else:
                hash_table[i] = 1
        return False