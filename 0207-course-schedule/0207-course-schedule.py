class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        done = set()
        def dfs(i, check):
            if i not in graph or i in done:
                done.add(i)
                return True
            if i in check:
                return False
            check.add(i)
            for pre in graph[i]:
                if not dfs(pre, check):
                    return False
            done.add(i)
            return True
            
        for i in range(numCourses):
            if not dfs(i, set()):
                return(False)
        return(True)