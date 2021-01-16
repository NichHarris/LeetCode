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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode output = new ListNode(0);
        ListNode first = l1, second = l2, current = output;
        int sum = 0;
        int carry = 0;
        while(first != null || second != null){
            int x = (first != null ? first.val : 0);
            int y = (second != null ? second.val : 0);
            sum = carry + x + y;
            if(sum >= 10){
                carry = 1;
            } else{
                carry = 0;
            }
            sum %= 10;
            current.next = new ListNode(sum);
            current = current.next;
            if(first != null) first = first.next;
            if(second != null) second = second.next;
        }
        if(carry > 0){
            current.next = new ListNode(carry);
        }
        return output.next;
    }
}