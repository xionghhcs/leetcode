"""
通过这道题来重新实现各种基本的排序算法
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.heapSort(nums)
     
    def heapSort(self, nums):
        def creatHeap(data, lastIdx):
            for i in range((lastIdx + 1)//2 - 1, -1, -1):
                t = i
                while 2 * t + 1 <= lastIdx:
                    bigIdx = 2 * t + 1
                    if bigIdx < lastIdx and data[bigIdx] < data[bigIdx + 1]:
                        bigIdx += 1
                    if data[t] < data[bigIdx]:
                        data[t], data[bigIdx] = data[bigIdx], data[t]
                        t = bigIdx
                    else:
                        break

        for i in range(len(nums)):
            creatHeap(nums, len(nums) - 1 - i)
            nums[0], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[0]

    def selectSort(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

    def insertSort(self, nums):
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
 
    def bubbleSort(self, nums):
        for i in range(1, len(nums)):
            for j in range(len(nums) - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
    
    def quickSort(self, nums, l, r):
        if l < r:
            i, j, pivot = l, r, nums[l]
            while i < j:
                while i < j and nums[j]>=pivot:
                    j -= 1
                if i < j:
                    nums[i] = nums[j]
                    i += 1
                while i < j and nums[i] < pivot:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            nums[i] = pivot
            self.quickSort(nums, l, i - 1)
            self.quickSort(nums, i + 1, r)

    def mergeSort(self, nums):
            
        def merge(nums, l, mid, r):
            tmp_array = [0] * (r - l + 1)
            idx = 0
            i, j = l, mid+1
            while i<=mid and j <= r:
                if nums[i] < nums[j]:
                    tmp_array[idx] = nums[i]
                    idx += 1
                    i += 1
                else:
                    tmp_array[idx] = nums[j]
                    idx += 1
                    j += 1
            while i <= mid:
                tmp_array[idx] = nums[i]
                idx += 1
                i += 1
            while j <= r:
                tmp_array[idx] = nums[j]
                idx += 1
                j += 1
            for i in range(idx):
                nums[l + i] = tmp_array[i]
        
        def sort(nums, l, r):
            if l == r:
                return 
            mid = (l + r) // 2
            sort(nums, l, mid)
            sort(nums, mid+1, r)
            merge(nums, l, mid, r)
        
        sort(nums, 0, len(nums) - 1)