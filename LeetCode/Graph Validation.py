class Solution(object):
    def validTree(self,n, edges):
        if len(edges) != n - 1:
            return False
        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,
        print neighbors
        def visit(v):
            map(visit, neighbors.pop(v, []))
        visit(0)
        return not neighbors


print Solution().validTree(5,[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])