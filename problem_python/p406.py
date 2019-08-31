class Solution:
    def reconstructQueue(self, data: List[List[int]]) -> List[List[int]]:
        data.sort(key=lambda x: (x[0], -x[1]), reverse=True, )
        for i in range(1, len(data)):
            tmp = data[i]
            idx = tmp[1]
            for j in range(i, idx, -1):
                data[j], data[j-1] = data[j-1], data[j]
            data[idx] = tmp
        return data