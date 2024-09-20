 Given the head of a linked list, remove the nth node from the end of the list and return its head.


 Input: head = [1,2,3,4,5], n = 2
 Output: [1,2,3,5]
 Example 2:

 Input: head = [1], n = 1
 Output: []
 Example 3:

 Input: head = [1,2], n = 1
 Output: [1]


public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        ListNode headPtr = head;
        int length = findLength(head);
        if(length-n-1 == -1) return head.next;
        int i = 0;
        while(i < length-n-1){
            i++;
            head = head.next;
        }
        head.next = head.next.next;

        return headPtr;
    }

    private int findLength(ListNode node){
        int length = 0;
        ListNode curr = node;
        while(curr != null){
            length++;
            curr = curr.next;
        }
        return length;
    }
}