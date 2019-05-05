class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid] and nums[mid] < nums[r] or \
                nums[l]<=target and target < nums[mid] or \
                nums[mid] < nums[r] and target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return -1

class Solution2:
    def search(self, nums, target):
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[j]:
                if nums[mid] < target and target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
                pass
            else:
                if nums[i] <= target and target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
                pass
        return -1
