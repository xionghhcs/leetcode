class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        ans = []
        q = collections.deque([kill])
        table = dict()
        for p, c in zip(ppid, pid):
            if p not in table:
                table[p] = []
            table[p].append(c)
        
        while len(q):
            n = q.popleft()
            ans.append(n)
            if n in table:
                q.extend(table[n])
        return ans
    