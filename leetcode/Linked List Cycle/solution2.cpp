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
        ListNode *node = head;
        ListNode *temp = head;
        int i = 0;
        while (node != NULL) {
            node = node->next;
            if (node == temp)
                return true;
            i++;
            // is a power of two
            if ((i & (i - 1)) == 0)
                temp = node;
        }
        return false;
    }
};
