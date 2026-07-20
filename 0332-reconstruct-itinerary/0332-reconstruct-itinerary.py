class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = collections.defaultdict(list)
        for a, b in sorted(tickets):
            dic[a].append(b)
        
        route = []
        def dfs(a):
            while dic[a]:
                dfs(dic[a].pop(0))
            route.append(a)
        
        dfs('JFK')
        return route[::-1]
        