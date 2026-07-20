class Solution:
    def smallestSubsequence(self, s: str) -> str:
        indices = {}
        for i in range(len(s)):
            indices[s[i]] = i

        stack = []
        seen = set()
        for i in range(len(s)):
            # skip duplicate characters
            if s[i] in seen:
                continue

            # check if u can remove the top char
            while stack and s[i] < stack[-1] and indices[stack[-1]] > i:
               seen.remove(stack[-1])
               stack.pop()

            stack.append(s[i])
            seen.add(s[i])

        return "".join(stack)