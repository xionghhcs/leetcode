
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            index = i - 1
            while nums[index] != 0:
                tmp = nums[index]
                nums[index] = 0
                index = tmp -1
        ans = []
        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(i + 1)
        return ans
