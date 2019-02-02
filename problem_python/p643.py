class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        tmp_sum = sum(nums[:4])
        i = 0
        ans = tmp_sum
        for j in range(k, len(nums)):
            tmp_sum = tmp_sum - nums[i] + nums[j]
            if tmp_sum > ans:
                ans = tmp_sum
            i += 1
        return float(ans) / k
