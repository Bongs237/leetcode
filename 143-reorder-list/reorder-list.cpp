/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/*
1 -> 2 -> 3 -> 4
i    j

1 2 3 4
i      

1* -> 2* -> 3 -> 4 -> 5 -> 6
1, 2, 3, 4, 5, 6 
 2, 3, 4, 5, 6
 3, 4, 5, 6
 4, 5, 6
 5, 6
 6
 
1 2 3 4
1 4 2 3
*/


//can't access the end, no side 
//while loop until pointer->next == nullptr;
//
 
class Solution {
public:
    void reorderList(ListNode* head)
    {
        stack<ListNode*> st;
           
        ListNode* original = head;
        ListNode* addToStack = head;
        while (addToStack != nullptr) {
            st.push(addToStack);
            addToStack = addToStack->next;
        }
        //1,2,3,4
        //elements = 2
        //4,3,2,1 = st
        //temp = 4
        //4->2
        //1->4->2->3->4
        //elements = 1
        //3,2,1
        //original = 2
        //temp = 3
        //2,1
        //1->4->2
        //3->
        
        int elementsLeftToPop = st.size() / 2;
        
        while(original != nullptr && elementsLeftToPop != 0)
        {
            ListNode* temp = st.top(); // 5
            st.pop();
            temp->next = original->next; // 5->2
            original->next = temp; // 1->5->2
            elementsLeftToPop--;
            
            original = original->next->next;
        }
        
        original->next = nullptr;
    }
};