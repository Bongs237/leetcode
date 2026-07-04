class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        queue = deque()
        adj = {}

        for road in roads:
            if road[0] not in adj:
                adj[road[0]] = []

            if road[1] not in adj:
                adj[road[1]] = []

            adj[road[0]].append([road[1], road[2]])
            adj[road[1]].append([road[0], road[2]])

        visited = set()
        visited.add(1)
        queue.appendleft(1)
        connected = []

        # ans = basically the lowest path out of all the edges connected to node 1
        ans = 10000000 # big number it will never hit

        while queue:
            curr = queue.popleft()
            for child, dist in adj[curr]:
                # sneaky sneaky line:
                # you're gonna traverse every connected node once bc of the if statement
                # but you ALSO traverse already visited children and do nothing
                # so then putting this line here allows u to get all the adjacent nodes to the current node
                # essentially getting every edge distance
                # smth like that
                ans = min(ans, dist)
                if child not in visited:
                    visited.add(child)
                    queue.appendleft(child)
                    connected.append(child)

        return ans