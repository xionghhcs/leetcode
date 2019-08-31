class Solution:
    def minMeetingRooms(self, data: List[List[int]]) -> int:
        import heapq
        q = []
        ans = 0
        data.sort()
        for item in data:
            if len(q) == 0:
                ans += 1
                heapq.heappush(q, item[1])
            else:
                if item[0] >= q[0]:
                    heapq.heappop(q)
                    heapq.heappush(q, item[1])
                else:
                    ans += 1
                    heapq.heappush(q, item[1])
        return ans
