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

        # all the elements pointing back to that element
        back = [[] for i in range(n)]
        for u, v in invocations:
            back[v].append(u)

        print(back)

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

        for ele in sus:
            back_pointing = back[ele]

            for pointer in back_pointing:
                if pointer not in sus:
                    can_remove = False
                    break

        if not can_remove:
            return [i for i in range(n)]
        else:
            return [i for i in range(n) if i not in sus]