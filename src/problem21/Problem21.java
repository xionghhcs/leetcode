/*
* 21. Merge Two Sorted Lists
*
* Author: xionghh
*
* Date: 2018-04-01
* */

package problem21;

public class Problem21 {
    public static void main(String[] args) {

    }
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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0);
        ListNode rear = res;
        while(l1 != null && l2 != null){
            if(l1.val < l2.val){
                ListNode tmp = new ListNode(l1.val);
                rear.next = tmp;
                rear = tmp;
                l1 = l1.next;
            }
            else{
                ListNode tmp = new ListNode(l2.val);
                rear.next = tmp;
                rear = tmp;
                l2 = l2.next;
            }
        }
        while(l1 != null){
            ListNode tmp = new ListNode(l1.val);
            rear.next = tmp;
            rear = tmp;
            l1 = l1.next;
        }
        while(l2 != null){
            ListNode tmp = new ListNode(l2.val);
            rear.next = tmp;
            rear = tmp;
            l2 = l2.next;
        }
        res = res.next;
        return res;
    }
}