/*
* 23. Merge k Sorted Lists
*
* Author : xionghh
*
* Date : 2018-04-07
* */
package problem23;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Problem23 {
    public static void main(String[] args) {

    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
 }

/*
* 两两归并
* */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 1){
            return lists[0];
        }
        else if(lists.length == 0){
            return null;
        }
        /*
        不能使用下面这种数组转list的做法，因为这样转化成了一个固定长度的list，不可修改
        List<ListNode> new_lists = Arrays.asList(lists);
        */
        List<ListNode> new_lists = new ArrayList<>(Arrays.asList(lists));
        while(new_lists.size()>1){
            int list_len = new_lists.size();
            for(int i=0;i<list_len;i=i+2){
                if(i+1<list_len){
                    ListNode tmp = mergerTowLists(new_lists.get(i), new_lists.get(i+1));
                    new_lists.add(tmp);
                }
                else{
                    ListNode tmp =mergerTowLists(new_lists.get(i),null);
                    new_lists.add(tmp);
                }
            }
            new_lists = new_lists.subList(list_len,new_lists.size());
        }
        return new_lists.get(0);
    }

    ListNode mergerTowLists(ListNode l1, ListNode l2){
        ListNode head = new ListNode(0);
        ListNode h = head;
        while(l1 !=null && l2 != null){
            if(l1.val<l2.val){
                h.next = l1;
                h = l1;
                l1 = l1.next;
            }
            else{
                h.next = l2;
                h = l2;
                l2 = l2.next;
            }
        }
        while(l1!= null){
            h.next = l1;
            h = l1;
            l1 = l1.next;
        }
        while(l2 != null){
            h.next = l2;
            h = l2;
            l2=l2.next;
        }
        head = head.next;
        return head;
    }
}

/*
* 该做法超时，可以通过129/130个case
* 假设lists数量是n，每隔list的长度是m，时间复杂度大概max(m)*log(n)
* */
class Solution2 {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 1){
            return lists[0];
        }
        else if(lists.length == 0){
            return null;
        }
        ListNode res = lists[0];
        for(int i=1;i<lists.length;i++){
            res = mergerTowLists(res, lists[i]);
        }
        return res;
    }

    ListNode mergerTowLists(ListNode l1, ListNode l2){
        ListNode head = new ListNode(0);
        ListNode h = head;
        while(l1 !=null && l2 != null){
            if(l1.val<l2.val){
                h.next = l1;
                h = l1;
                l1 = l1.next;
            }
            else{
                h.next = l2;
                h = l2;
                l2 = l2.next;
            }
        }
        while(l1!= null){
            h.next = l1;
            h = l1;
            l1 = l1.next;
        }
        while(l2 != null){
            h.next = l2;
            h = l2;
            l2=l2.next;
        }
        head = head.next;
        return head;
    }
}

