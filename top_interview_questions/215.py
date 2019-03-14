class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)

        if k > len(nums):
            return -1

        return nums[k - 1]


class Solution2:
    def findKthLargest(self, nums, k):
        if nums is None or k < 0 or len(nums) == 0:
            return None
        
        def partition(nums, left, right):
            pivot = nums[left]
            l = left + 1
            r = right
            while l <= r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[left], nums[r] = nums[r], nums[left]
            return r
        
        left = 0
        right = len(nums) - 1
        while True:
            mid = partition(nums, left, right)
            if mid == k - 1:
                return nums[mid]
            elif mid > k - 1:
                right = mid - 1
            else:
                left = mid + 1
        
                
class Solution3:
    def findKthLargest(self, nums, k):
        import heapq
        nums = list(map(lambda x: -x, nums))
        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(k)
        
        return nums[0]

