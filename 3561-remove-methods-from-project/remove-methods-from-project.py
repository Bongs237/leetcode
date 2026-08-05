class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        """
        0: 1
        1: 2
        2: -
        3: 2

        1 <- 0

        """

        sus = set()
        adj = [[] for i in range(n)]
        for u, v in invocations:
            adj[u].append(v)

        def bfs(src):
            queue = deque()

            queue.append(src)
            sus.add(src)

            while queue:
                curr = queue.popleft()

                for child in adj[curr]:
                    if child not in sus:
                        sus.add(child)
                        queue.append(child)

        bfs(k)

        can_remove = True
        for u, v in invocations:
            # If there is an edge that goes from non sus to sus, that sus element can't be removed
            # And from problem statement, that means you should NOT remove any elements anymore
            if u not in sus and v in sus:
                can_remove = False
                break

        if can_remove:
            return [i for i in range(n) if i not in sus]
        else:
            return [i for i in range(n)]