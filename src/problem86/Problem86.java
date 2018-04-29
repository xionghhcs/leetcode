/*
* 86. Partition List
*
* Author : xionghh
*
* Date : 2018-04-29
* */
package problem86;

public class Problem86 {
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
    public ListNode partition(ListNode head, int x) {
        ListNode less = new ListNode(0);
        ListNode less_rear = less;
        ListNode greater = new ListNode(0);
        ListNode greater_rear = greater;
        while(head!=null){
            if(head.val<x){
                less_rear.next = head;
                less_rear = less_rear.next;
            }
            else{
                greater_rear.next = head;
                greater_rear = greater_rear.next;
            }
            head = head.next;
        }
        greater_rear.next= null;
        less_rear.next = greater.next;
        head = less.next;
        return head;
    }
}

