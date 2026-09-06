# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        n = 0

        while curr:
            stack.append(curr)
            curr = curr.next
            n += 1

        curr = head

        for i in range(n // 2):
            orig_next = curr.next
            curr.next = stack.pop()
            curr.next.next = orig_next
            curr = orig_next

        curr.next = None