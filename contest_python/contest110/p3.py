class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 从小到大排序
        points.sort(lambda x: (x[0], x[1]), reverse=True)
        print(points)
        flag = [[0] * 501] * 501



        return 0
