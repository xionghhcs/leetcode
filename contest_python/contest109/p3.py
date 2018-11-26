class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # 先找到一个小岛
        l = len(A)
        for idx in range(l):
            item = [0] + A[idx] + [0]
            A[idx] = item
        l += 2

        A = [[0] * l] + A + [[0] * l]

        for i in range(l):
            flag = False
            for j in range(l):
                if A[i - 1][j] == 0 and A[i + 1][j] == 0 and A[i][j - 1] == 0 and A[i][j + 1] == 0:
                    xx = i
                    yy = j
                    flag = True
                    break
            if flag is True:
                break
        A[xx][yy] = 2
        self.ans = 160
        self.find(A, xx, yy, cnt=0)
        return self.ans

    def find(self, A, x, y, cnt=0):
        l = len(A) - 1
        if A[x][y] == 1:
            if cnt < self.ans:
                self.ans = cnt
        else:
            if x - 1 >= 1 and A[x - 1][y] == 0:
                A[x - 1][y] = 2
                self.find(A, x - 1, y, cnt + 1)

            if x + 1 < l and A[x + 1][y] == 0:
                A[x + 1][y] = 2
                self.find(A, x + 1, y, cnt + 1)

            if y - 1 >= 1 and A[x][y - 1] == 0:
                A[x][y - 1] = 2
                self.find(A, x, y - 1, cnt + 1)

            if y + 1 < l and A[x][y + 1] == 0:
                A[x][y + 1] = 2
                self.find(A, x, y + 1, cnt + 1)
