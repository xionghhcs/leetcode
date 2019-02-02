
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        p = [item.append(item[0]**2 + item[1]**2) for item in points]
        sorted(p, key=lambda x: x[-1])
        p = p[:K]
        p = [p[:2] for item in p]
        return p
