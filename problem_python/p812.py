class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        import math
        def get_dist(a, b):
            return math.sqrt((abs(a[0] - b[0])) ** 2 + (abs(a[1] - b[1]) )** 2)
        
        ans = 0
        for i in points:
            for j in points:
                for k in points:
                    if i == j or i == k or j == k:
                        continue
                    
                    d1 = get_dist(i, j)
                    d2 = get_dist(i, k)
                    d3 = get_dist(j, k)

                    if d1+d2 < d3 or d1+d3<d2 or d2+d3<d1:
                        continue
                    p = (d1 + d2 + d3) / 2
                    area = (p * (p - d1)*(p-d2)*(p-d3)) ** 0.5
                    if area > ans :
                        ans = area
        return ans