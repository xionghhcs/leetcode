class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        ans = 0
        for i in range(len(self.nums)):
            ans += self.nums[i]
            self.nums[i] = ans
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i - 1]