/*
* 19. Remove Nth Node From End of List
*
* Author : xionghh
*
* Date : 2018-04-06
* */
package problem19;

public class Problem19 {
}

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class ListNode {
     int val;
     ListNode next;
     ListNode(int x) { val = x; }
}

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode r=head;
        while(n>0){
            r=r.next;
            n--;
        }
        ListNode h=head;
        ListNode h_pre=null;
        while(r!=null){
            h_pre = h;
            h=h.next;
            r=r.next;
        }
        if(h == head){
            head=head.next;
        }
        else{
            h_pre.next = h.next;
        }
        return head;
    }
}