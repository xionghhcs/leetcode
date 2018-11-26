class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        data_size = len(A)
        sum_list = []
        for idx in range(data_size):
            sum_list.append([0] * data_size)

        for i in range(data_size):
            for j in range(data_size):
                if i == 0:
                    sum_list[i][j] = A[i][j]
                else:
                    if j - 1 >= 0:
                        tmp1 = A[i][j] + sum_list[i-1][j-1]
                    else:
                        tmp1 = 100 * 100 * 100 + 1

                    tmp2 = A[i][j] + sum_list[i-1][j]

                    if j+1 < data_size:
                        tmp3 = A[i][j] + sum_list[i-1][j+1]
                    else:
                        tmp3 = 100 * 100 * 100 + 1
                    sum_list[i][j] = min(tmp1, tmp2, tmp3)

        return min(sum_list[-1])



if __name__ == '__main__':
    t = Solution()
    A = [[-19,57],[-40,-5]]
    res = t.minFallingPathSum(A)
    print(res)
    pass