
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

class Solution2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        data = [(item[0]**2 + item[1]**2, item[0], item[1]) for item in points]
        def quick(data, i, j):
            if i > j:
                return 
            l = i
            r = j
            tmp = data[i]
            while i < j:
                while i < j and data[j][0] >= tmp[0]:
                    j -= 1
                if i < j:
                    data[i] = data[j]
                while i < j and data[i][0] <= tmp[0]:
                    i += 1
                if i < j:
                    data[j] = data[i]
            data[i] = tmp
            if i == K:
                return
            elif i < K:
                quick(data, i + 1, r)
            else:
                quick(data, l, i - 1)
                
        quick(data, 0, len(data) - 1)
        ans = []
        for i in range(K):
            ans.append([data[i][1], data[i][2]])
        return ans
    