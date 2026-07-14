# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        cycle = False
        while slow and fast and fast.next:
            print(slow.val, fast.val)

            slow = slow.next
            fast = fast.next
            fast = fast.next
            
            if slow is fast:
                cycle = True
                break

        if not cycle:
            return None

        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow