/*
* 53. Maximum Subarray
*
* Author : xionghh
*
* Date : 2018-04-01
* */

package problem53;

public class Problem53 {
    public static void main(String[] args) {

    }
}

/*
* 分治法求解
* */
class Solution {
    public int maxSubArray(int[] nums) {
        return findMaxSubArray(nums, 0, nums.length-1);
    }

    private int findMaxSubArray(int [] A, int low, int high){
        if(low == high){
            return A[low];
        }
        else{
            int mid = (low + high) / 2;
            int left_sum = findMaxSubArray(A, low, mid);
            int right_sum = findMaxSubArray(A, mid+1, high);
            int cross_sum = findMaxCrossingSubArray(A, low, mid, high);
            return Math.max(Math.max(left_sum, right_sum), cross_sum);
        }
    }

    private int findMaxCrossingSubArray(int A[], int low, int mid, int high){
        int left_sum = Integer.MIN_VALUE;
        int sum = 0;
        for(int i = mid; i>=low;i--){
            sum += A[i];
            if(sum > left_sum){
                left_sum = sum;
            }
        }
        int right_sum=Integer.MIN_VALUE;
        sum = 0;
        for(int j= mid+1;j<=high;j++){
            sum += A[j];
            if(sum > right_sum){
                right_sum = sum;
            }
        }
        return left_sum + right_sum;
    }
}

/*
* 暴力求解的方法
*
* 在leetcode上，这题直接用暴力是会超时的。
* */
class Solution2{
    public int maxSubArray(int[] nums) {
        int max_sum = Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++){
            int sum = 0;
            for(int j=i;j<nums.length;j++){
                sum += nums[j];
                if(sum > max_sum){
                    max_sum= sum;
                }
            }
        }
        return max_sum;
    }
}