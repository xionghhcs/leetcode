class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uset = [i for i in range(len(edges) + 1)]
        
        def find(k):
            while uset[k] != k:
                k = uset[k]
            return k
        
        def union(i,j):
            uset[j] = i
        
        for e in edges:
            start = e[0]
            end = e[1]
            s_p = find(start)
            e_p = find(end)
            if s_p == e_p:
                return e
            union(s_p, e_p)
            