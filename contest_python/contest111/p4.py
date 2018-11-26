"""
Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.


"""


class Solution:
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        common = []
        common2 = []
        for str1 in A:
            row = []
            row2 = []
            for str2 in A:
                l = min(len(str1), len(str2))
                max_len = 0
                max_len2 = 0
                for idx in range(1, l):
                    if str1[:idx] == str2[-idx:]:
                        max_len = idx
                    if str2[:idx] == str1[-idx:]:
                        max_len2 = idx
                row.append(max_len)
                row2.append(max_len2)

            common.append(row)
            common2.append(row2)
        print(common)
        print(common2)
        return ''