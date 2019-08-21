class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums)-2):
            l,r = i+1, len(nums) - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if abs(cur - target)<abs(ans - target):
                    ans = cur
                if cur == target:
                    return cur
                
                if cur < target:
                    l += 1
                else:
                    r -= 1
        return ans
