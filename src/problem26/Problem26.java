/*
* 26. Remove Duplicates from Sorted Array
*
* Author : xionghh
*
* Date : 2018-04-07
* */

package problem26;

public class Problem26 {
}

/*
* 一个小技巧，将所有重复数字设置为nums[0]-1，作为哨兵，碰到哨兵就退出循环。但是需要注意-1是是否会导致整数溢出。
*
* 这个方法每次都要移动数组，时间复杂度有点高。
* */
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0 || nums.length == 1) {
            return nums.length;
        }
        int res = 1;
        int i = 1;
        while (i < nums.length) {
            if ( nums[i] == nums[0] -1){
                break;
            } else if (nums[i] == nums[i - 1]) {
                int j = i;
                while(j<nums.length-1){
                    nums[j] = nums[j+1];
                    j++;
                }
                nums[j] = nums[0]-1;
                continue;
            }
            res += 1;
            i += 1;
        }
        return res;
    }
}

/*
* 不需要移动数组，常量空间复杂度
* */
class Solution2{
    public int removeDuplicates(int[] nums) {
        if(nums.length<2){
            return nums.length;
        }
        int id=1;
        for(int i=1;i<nums.length;i++){
            if(nums[i]!=nums[i-1]) nums[id++] = nums[i];
        }
        return id;
    }
}