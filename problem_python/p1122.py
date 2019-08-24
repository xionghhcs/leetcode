class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = [0] * len(arr1)
        table = dict()
        for c in arr1:
            table[c] = table.get(c, 0) + 1
        idx = 0
        for c in arr2:
            for _ in range(table[c]):
                ans[idx] = c
                idx += 1
            del table[c]
        q = []
        import heapq
        for k in table:
            heapq.heappush(q, [k, table[k]])
        while len(q) > 0:
            top = heapq.heappop(q)
            for _ in range(top[1]):
                ans[idx] = top[0]
                idx += 1
        return ans
        