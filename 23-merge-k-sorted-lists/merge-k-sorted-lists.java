/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    ListNode newPtr;

    // just link the actual node
    public void add(ListNode node) {
        newPtr.next = node;
        newPtr = newPtr.next;
    }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }

        // Make dummy node
        ListNode dummy = new ListNode(0);

        ListNode pt1 = list1;
        ListNode pt2 = list2;

        newPtr = dummy;

        // Basically it's a race
        // If first one smaller, move first pointer
        // If second one smaller, move second one type thing
        while (pt1 != null && pt2 != null) {
            if (pt2.val < pt1.val) {
                add(pt2);
                pt2 = pt2.next;
            } else {
                add(pt1);
                pt1 = pt1.next;
            }
        }

        // until one of them is null
        while (pt1 != null) {
            add(pt1);
            pt1 = pt1.next;
        }
        while (pt2 != null) {
            add(pt2);
            pt2 = pt2.next;
        }

        return dummy.next;
    }

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        if (lists.length == 1) return lists[0];

        ListNode theList = lists[0];
        System.out.println(theList == null);
        for (int i = 1; i < lists.length; i++) {
            theList = mergeTwoLists(theList, lists[i]);
        }
        return theList;
    }
}