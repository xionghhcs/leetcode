class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        def find_next(i, nums):
            idx = 0
            while nums[idx] != i:
                idx += 1
            for index in range(idx+1, len(nums)):
                if nums[index] > i:
                    return nums[index]
            return -1
        
        ans = []
        for i in findNums:
            ans.append(find_next(i, nums))
        return ans
