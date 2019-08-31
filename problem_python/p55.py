class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                break
            reach = max(reach, i + nums[i])
            if reach >= len(nums)-1:
                return True
        return False
    