class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 선수과목 그래프에 사이클이 존재하면 False
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        visiting = set()

        def dfs(cur):
            if cur in visiting:
                return False # 사이클
            if cur in visited:
                return True # 사이클 없이 완료 가능함을 이미 확인
            visiting.add(cur)
            for nxt in graph[cur]:
                if not dfs(nxt):
                    return False
            visiting.remove(cur)
            visited.add(cur)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True