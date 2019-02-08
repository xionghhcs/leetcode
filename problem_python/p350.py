class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0:
            return nums1
        if len(nums2) == 0:
            return nums2
        nums1.sort()
        nums2.sort()
        i, j, k = 0,0,0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i]< nums2[j]:
                i += 1
            else:
                nums1[k] = nums1[i]
                k += 1
                i += 1
                j += 1
        return nums1[:k]

