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

class Solution2:
    def intersect(self, n1: List[int], n2: List[int]) -> List[int]:
        ans = []
        n1.sort()
        n2.sort()
        i = 0
        j = 0
        while i<len(n1) and j<len(n2):
            if n1[i] == n2[j]:
                ans.append(n1[i])
                i += 1
                j += 1
                continue
            if n1[i] < n2[j]:
                i += 1
            else:
                j += 1
        return ans
      
        