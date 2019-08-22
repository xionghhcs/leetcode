# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 0, n - 1

        while i < j:
            mid = int((i + j) / 2)
            if isBadVersion(mid + 1) :
                j = mid - 1
            else:
                i = mid + 1
        if isBadVersion( i + 1) is False:
            return i + 2
        else:
            return i + 1

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            if left == right:
                return left
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
