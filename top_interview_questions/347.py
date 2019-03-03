class Skill(object):
    def __init__(self,priority,description):
        self.priority = priority
        self.description = description
    def __lt__(self,other):#operator < 
        return self.priority < other.priority
    def __ge__(self,other):#oprator >=
        return self.priority >= other.priority
    def __le__(self,other):#oprator <=
        return self.priority <= other.priority
    def __cmp__(self,other):
        #call global(builtin) function cmp for int
        return cmp(self.priority,other.priority)
    def __str__(self):
        return '(' + str(self.priority)+',\'' + self.description + '\')'


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import operator
        table = dict()
        for v in nums:
            if v in table:
                table[v]  += 1
            else:
                table[v] = 1
        sorted_data = sorted(table.items(), key=operator.itemgetter(1), reverse=True)
        ans = []
        for i in range(k):
            ans.append(sorted_data[i][0])
        return ans


class Solution2:
    def topKFrequent(self, nums, k):
        bucket, table = [],{}
        for v in nums:
            table[v] = table[v] + 1 if v in table else 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key in table:
            bucket[table[key]].append(key)
        
        ans = []
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i] != []:
                ans.extend(bucket[i])
            if len(ans) >= k:
                break
        return ans[:k]

class Solution3:
    def topKFrequent(self, nums, k):
        import heapq
        table = {}
        for v in nums:
            table[v] = table[v] + 1 if v in table else 1
        h = []
        for key in table:
            heapq.heappush(h, (-table[key], key))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(h)[1])
        return ans


class Solution4:
    def topKFrequent(self, nums, k):
        import collections
        cnt = collections.Counter(nums)
        return [item[0] for item in cnt.most_common(k)]

