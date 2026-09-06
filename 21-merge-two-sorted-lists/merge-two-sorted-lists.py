# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None

        i = list1
        j = list2
        k = None
        head = None

        if i and j:
            if i.val < j.val:
                k = list1
                i = i.next
            else:
                k = list2
                j = j.next

            head = k
        elif i and not j:
            head = i
            i = i.next
            k = head
        else:
            head = j
            j = j.next
            k = head

        while i and j:
            if i.val < j.val:
                k.next = i
                i = i.next
            else:
                k.next = j
                j = j.next

            k = k.next

        while i:
            k.next = i
            k = k.next
            i = i.next

        while j:
            k.next = j
            k = k.next
            j = j.next

        return head