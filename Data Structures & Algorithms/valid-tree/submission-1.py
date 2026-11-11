from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        seen = set()
        def dfs(cur):
            seen.add(cur)
            for nei in adj[cur]:
                if nei not in seen:
                    dfs(nei)
        dfs(0)
        return len(seen) == n
                