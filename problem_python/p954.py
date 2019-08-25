class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        table = dict()
        for c in A:
            table[c] = table.get(c, 0) + 1
        data = [(abs(c), c) for c in A]
        data.sort()
        cnt = 0
        for idx in range(len(A)):
            item = data[idx]
            c = item[1]
            if table[c] == 0:
                continue
            if 2 * c not in table:
                return False
            if table[2 * c] > 0:
                table[2 * c] -= 1
                table[c] -= 1
            else:
                return False
            cnt += 2
        return cnt == len(A)
    