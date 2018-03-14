/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *node1 = head;
        ListNode *node2 = head;
        while (node2 != NULL && node2->next != NULL) {
            node2 = node2->next->next;
            node1 = node1->next;
            if (node1 == node2) {
                return true;
            }
        }
        return false;
    }
};
