class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0
        while idx < len(arr):
            if arr[idx] == 0:
                if idx + 1 < len(arr):
                    j = len(arr) - 1
                    while j > idx:
                        arr[j] = arr[j-1]
                        j -= 1
                idx += 1
            idx += 1
        return arr
    