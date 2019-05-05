class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = dict()
        for v in nums:
            table[v] = table.get(v, 0) + 1
        ans = sorted(table.items(), key=lambda x: x[1], reverse=True)
        return [ans[i][0] for i in range(k)]
