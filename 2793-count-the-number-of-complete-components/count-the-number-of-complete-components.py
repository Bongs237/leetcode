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

        # Jank class
        class Pair:
            def __init__(self, m, n):
                self.m = m
                self.n = n

            def __str__(self):
                return "Pair[" + str(self.m) + ", " + str(self.n) + "]"

            def __repr__(self):
                return str(self)

            def __eq__(self, other):
                return (self.m == other.m and self.n == other.n) or (self.m == other.n and self.n == other.m)

            def __hash__(self):
                return hash(str(min(self.m, self.n)) + " " + str(max(self.m, self.n)))

        # global
        visited = set()
        comp = []

        def bfs(src):
            visited = set()
            queue = deque()

            queue.append(src)
            visited.add(src)

            while queue:
                curr = queue.popleft()
                for child in adj[curr]:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)

            is_complete = True
            for node in visited:
                if len(adj[node]) != len(visited) - 1:
                    is_complete = False
                    break

            return visited, is_complete

        adj = [[] for i in range(n)]
        edge_pairs = set()
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            edge_pairs.add(Pair(edge[0], edge[1]))

        ans = 0
        for i in range(n):
            if i not in visited:
                vis_for_node, is_complete = bfs(i)
                visited.update(vis_for_node)
                comp.append(vis_for_node)
                if is_complete:
                    ans += 1

        return ans