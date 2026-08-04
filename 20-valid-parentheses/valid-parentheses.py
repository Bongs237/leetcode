class Solution:
    def isValid(self, s: str) -> bool:
        closer = ")]}"
        opener = "([{"
        stack = []

        for ch in s:
            if ch in opener:
                stack.append(ch)
            else: # closer
                if not stack or closer.index(ch) != opener.index(stack[-1]):
                    return False
                stack.pop()

        return not stack