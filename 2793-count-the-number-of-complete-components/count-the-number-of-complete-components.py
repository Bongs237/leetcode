class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        adj:
        0: 1, 2
        1: 0, 2
        2: 0, 1
        3: 4
        4: 3
        5: -

        Find connected components
        Eliminate components that are not complete
        """
        # global
        visited = set()
        comp = []

        def bfs(src):
            # We can use the global visited
            # cuz we call this at the start of a new connected component
            nonlocal visited
            queue = deque()

            queue.append(src)
            visited.add(src)

            nodes = 0
            total_adj_nodes = 0 # sum of the count of neighbors for each node

            while queue:
                curr = queue.popleft()
                nodes += 1
                total_adj_nodes += len(adj[curr])
                for child in adj[curr]:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)

            expected_total_adj_nodes = (nodes - 1) * nodes
            return expected_total_adj_nodes == total_adj_nodes

        adj = [[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        ans = 0
        for i in range(n):
            if i not in visited:
                if bfs(i):
                    ans += 1

        return ans