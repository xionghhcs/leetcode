/*
* 27. Remove Element
*
* Author : xionghh
*
* Date : 2018-04-08
* */

package problem27;

public class Problem27 {
}

class Solution {
    public int removeElement(int[] nums, int val) {
        int id=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i] == val) continue;
            nums[id++] = nums[i];
        }
        return id;
    }
}