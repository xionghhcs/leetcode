/*
* 25. Reverse Nodes in k-Group
*
* Author : xionghh
*
* Date : 2018-04-08
* */

package problem25;

public class Problem25 {
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
    public ListNode reverseKGroup(ListNode head, int k) {
        if(k == 1) return head;
        ListNode h_pre = new ListNode(0);
        h_pre.next = head;
        head = h_pre;
        ListNode h = null;
        ListNode h_post = h_pre;
        int n = k;
        while(n-->0 && h_post != null) h_post = h_post.next;
        while(h_post != null){
            ListNode tmp = null;
            h = h_pre.next;
            do{
                tmp = h.next;
                h.next = tmp.next;
                ListNode h_pre_next = h_pre.next;
                h_pre.next = tmp;
                tmp.next = h_pre_next;
            }while(tmp != h_post);
            h_pre = h;
            h_post = h_pre;
            n = k;
            while(n-->0 && h_post != null) h_post = h_post.next;
        }
        head = head.next;
        return head;
    }
}



