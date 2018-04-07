/*
* 24. Swap Nodes in Pairs
*
* Author : xionghh
*
* Date : 2018-04-07
* */
package problem24;

public class Problem24 {
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

/*
* 不合题目要求的一种做法,即直接修改node的值
* */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null){
            return null;
        }
        ListNode h = head;
        ListNode h_post = h.next;
        while(h_post != null){
            int val = h.val + h_post.val;
            h.val = h_post.val;
            h_post.val = val-h.val;
            h = h_post.next;
            if(h!=null){
                h_post = h.next;
            }
            else{
                break;
            }
        }
        return head;
    }
}

/*
* 不修改值，直接操作节点。技巧：在头部增加一个头节点，方便统一操作。
* */
class Solution2 {
    public ListNode swapPairs(ListNode head) {
        if(head == null){
            return null;
        }
        ListNode h = head;
        ListNode h_post = h.next;
        ListNode h_pre = new ListNode(0);
        h_pre.next = h;
        head = h_pre;
        while(h_post!=null){
            h_pre.next = h_post;
            h.next = h_post.next;
            h_post.next = h;
            h_pre = h;
            h = h.next;
            if(h == null){
                break;
            }
            h_post = h.next;
        }
        head = head.next;
        return head;
    }
}