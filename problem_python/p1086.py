class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        import heapq
        table = dict()
        for item in items:
            idx = item[0]
            if idx not in table:
                table[idx] = []
            heapq.heappush(table[idx], item[1])
            if len(table[idx])>5:
                heapq.heappop(table[idx])
        ans = []
        for k in table:
            scores = table[k]
            ans.append([k, sum(scores)//5])
        return ans
    