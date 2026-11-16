class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        visiting = set()
        done = set()
        def dfs(c):
            if c in visiting:
                return False
            
            if c in done:
                return True
            visiting.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            done.add(c)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True 