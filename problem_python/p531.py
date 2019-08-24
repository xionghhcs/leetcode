class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        row = [0] * len(picture)
        col = [0] * len(picture[0])
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
        cnt = 0
        for i in range(len(row)):
            if row[i] == 1:
                for j in range(len(col)):
                    if col[j] == 1 and picture[i][j] == 'B':
                        cnt += 1
        return cnt
    