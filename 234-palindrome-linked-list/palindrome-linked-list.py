# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        de = deque()
        curr = head
        n = 0

        while curr:
            de.append(curr.val)
            curr = curr.next
            n += 1

        for i in range(n // 2):
            left = de.popleft()
            right = de.pop()

            if left != right:
                return False

        return True
        