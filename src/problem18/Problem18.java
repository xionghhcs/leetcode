/*
* 18. 4Sum
*
* Author : xionghh
*
* Date : 2018-04-06
* */
package problem18;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Problem18 {
    public static void main(String[] args) {
        int [] nums= new int[]{-1,0,1,2,-1,-4};
        int target = -1;
        Solution so = new Solution();
        so.fourSum(nums, target);
    }
}

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            /*
            * 如果这个数之前找过了，就不用找了，防止重复
            * */
            if(i>0 && nums[i] == nums[i-1]){
                continue;
            }
            for(int j=i+1;j<nums.length;j++){
                /*
                * 如果这个数之前找过了，现在就不用找了，防止重复
                * */
                if(j>i+1 && nums[j] == nums[j-1]){
                    continue;
                }
                int begin = j+1;
                int end = nums.length-1;
                while(begin<end){
                    int sum = nums[i] + nums[j] + nums[begin] + nums[end];
                    if(sum == target){

                        List<Integer> tmp = new ArrayList<>();
                        tmp.add(nums[i]);
                        tmp.add(nums[j]);
                        tmp.add(nums[begin]);
                        tmp.add(nums[end]);
                        res.add(tmp);
                        int tmp_b = nums[begin];
                        int tmp_e = nums[end];
                        //防止重复
                        while(begin<end && nums[begin] == tmp_b) begin++;
                        while(begin<end && nums[end] == tmp_e) end--;
                    }
                    else if(sum<target){
                        begin++;
                    }
                    else{
                        end--;
                    }
                }
            }
        }
        return res;
    }
}

/*
[-3,-2,-1,0,0,1,2,3]
0
[-1,-5,-5,-3,2,5,0,4]
-7
[0,0,0,0]
0
[-1,0,1,2,-1,-4]
-1
*/