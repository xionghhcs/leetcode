class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - 1 - 1
        while idx >= 0:
            if nums[idx] < nums[idx + 1]:
                for j in range(len(nums)-1, idx, -1):
                    if nums[j] > nums[idx]:
                        nums[idx], nums[j] = nums[j], nums[idx]
                        break
                break
            idx -= 1

        i = idx + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        