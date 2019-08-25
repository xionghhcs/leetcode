class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        if len(nums) == 0:
            if upper - lower == 0:
                ans.append('{}'.format(upper))
            else:
                ans.append('{}->{}'.format(lower, upper))
            return ans
        
        
        if nums[0] > lower:
            if lower + 1 == nums[0]:
                ans.append('{}'.format(lower))
            else:
                ans.append('{}->{}'.format(lower, nums[0]-1))
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1]<= 1:
                continue
            elif nums[i] - nums[i-1] == 2:
                ans.append('{}'.format(nums[i] - 1))
            else:
                ans.append('{}->{}'.format(nums[i-1] + 1, nums[i] - 1))
        
        if nums[-1] < upper:
            if nums[-1] + 1 == upper:
                ans.append('{}'.format(upper))
            else:
                ans.append('{}->{}'.format(nums[-1] + 1, upper))
        
        
        return ans 