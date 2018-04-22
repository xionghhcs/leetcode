/*
* 33. Search in Rotated Sorted Array
*
* Author : xionghh
*
* Date : 2018-04-22
* */

package problem33;

public class Problem33 {
}

class Solution {
    public int search(int[] nums, int target) {
        for(int i=0;i<nums.length;i++){
            if(nums[i] == target){
                return i;
            }
        }
        return -1;
    }
}

class Solution2{
    public int search(int[] nums, int target){
        int i=0;
        int j=nums.length-1;
        while(i<j){
            int mid = (i+j)/2;
            if(nums[mid] == target){
                return mid;
            }
            if(nums[mid]>=nums[i]){
                if(target>=nums[i] && target<nums[mid]){
                    j=mid-1;
                }
                else{
                    i=mid+1;
                }
            }
            if(nums[mid]<nums[j]){
                if(target >nums[mid] && target < nums[j]){
                    i = mid + 1;
                }
                else{
                    j = mid - 1;
                }
            }
        }
        return -1;
    }
}