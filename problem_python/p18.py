class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            for j in range(i +1, len(nums)):
                cur_s = nums[i] + nums[j]
                l, r = j + 1, len(nums)-1
                while l < r:
                    tmp_s = nums[l] + nums[r] + cur_s
                    if tmp_s == target:
                        ans.append((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif tmp_s < target:
                        l += 1
                    else:
                        r -= 1
        
        return list(set(ans))
