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
