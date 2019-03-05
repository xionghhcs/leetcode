# 其中排序算法

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        冒泡
        """
        if nums is None:
            return None
        for i in range(1, len(nums)):
            j = i - 1
            tmp = nums[i]
            while j >=0 and nums[j] > tmp:
                nums[j+1] = nums[j]
                j -= 1
            if j < 0:
                nums[0] = tmp
            else:
                nums[j+1] = tmp
        return nums
