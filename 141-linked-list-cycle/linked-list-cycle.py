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
            # If one is going at 1x and another going at 2x
            # if there is a cycle,
            # eventually both will hit the same node at the same time
            if slow is fast:
                return True

            slow = slow.next
            if fast.next is None: # If we went off the end with fast, there is no cycle
                return False
            fast = fast.next.next
        
        return False