class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # 超时
        i = 0
        l = len(A)
        def get_ans(matrix, s, ans, row):
            for j in range(l):
                tmp = s + matrix[row][j]
                if row == 3:
                    if tmp == 0:
                        ans[0] += 1
                else:
                    get_ans(matrix, tmp, ans, row + 1)
        matrix = [A, B, C, D]
        ans = [0]
        get_ans(matrix, 0, ans, 0)
        return ans[0]
