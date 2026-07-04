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

        print(adj)

        visited = set()
        visited.add(1)
        queue.appendleft(1)
        connected = []

        while queue:
            curr = queue.popleft()
            for child, dist in adj[curr]:
                if child not in visited:
                    visited.add(child)
                    queue.appendleft(child)
                    connected.append(child)

        print(connected)

        ans = 10000000
        for connected_node in connected:
            print("on node", connected_node)
            for child, dist in adj[connected_node]:
                print("Looking at", child, dist)
                ans = min(ans, dist)

        return ans