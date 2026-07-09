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

        while slow and fast and fast.next:
            # If one is going at 1x and another going at 2x
            # if there is a cycle,
            # eventually both will hit the same node at the same time
            if slow is fast:
                return True

            slow = slow.next
            fast = fast.next.next
        
        return False