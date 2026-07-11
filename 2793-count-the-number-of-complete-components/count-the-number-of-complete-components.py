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
            #distance = [-1] * n
            visited = set()
            queue = deque()

            queue.append(src)
            visited.add(src)
            #distance[src] = 0

            while queue:
                curr = queue.popleft()
                for child in adj[curr]:
                    if child not in visited:
                        visited.add(child)
                        #distance[child] = distance[curr] + 1
                        #print(distance)
                        queue.append(child)

            return visited

        adj = [[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        for i in range(n):
            if i not in visited:
                print("callign bfs on",i)
                vis_for_node = bfs(i)
                visited.update(vis_for_node)
                comp.append(vis_for_node)

        ans = 0
        for nodes in comp:
            nodes = list(nodes)
            is_complete = True
            # o n cubed oh heck nah
            for i in range(len(nodes)):
                for j in range(i+1, len(nodes)):
                    first, second = nodes[i], nodes[j]
                    #print("testing", first, second)
                    if not([first, second] in edges or [second, first] in edges):
                        is_complete = False
                        break

            if is_complete:
                ans += 1

        return ans