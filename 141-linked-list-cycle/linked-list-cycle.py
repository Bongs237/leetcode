# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if head is None:
            return False

        fast = head.next

        while slow and fast:
            if slow is fast:
                return True

            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next.next
        
        return False