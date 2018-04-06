/*
* 16. 3Sum closest
*
* Author : xionghh
*
* Date : 2018-04-06
* */
package problem16;

import java.util.Arrays;

public class Problem16 {
    public static void main(String[] args) {

    }
}

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int res=0;
        boolean flag = true;
        boolean found = false;
        for(int i=0;i<nums.length;i++){
            int j=i+1;
            int k=nums.length-1;
            while(j<k){
                int sum = nums[i] + nums[j] + nums[k];
                if(flag){
                    flag = false;
                    res = sum;
                }
                if(sum == target){
                    res = sum;
                    found = true;
                    break;
                }
                else if(sum < target){
                    if(Math.abs(sum - target) < Math.abs(res - target)){
                        res= sum;
                    }
                    j++;
                }
                else{
                    if(Math.abs(sum - target) < Math.abs(res - target)){
                        res= sum;
                    }
                    k--;
                }
            }
            if(found){
                break;
            }
        }
        return res;
    }
}