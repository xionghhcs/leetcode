package problem4;
/*
* leetcode 4. Longest Substring Without Repeating Characters
*
* Author : xionghh
*
* Date : 2018-04-01
* */

public class Problem4 {
    public static void main(String[] args) {
        Solution so = new Solution();
        int [] nums1 = new int[]{1,2};
        int [] nums2 = new int[]{3,4};
        System.out.println(so.findMedianSortedArrays(nums1, nums2));
    }
}

/*
* 第一种方法，直接将两个数组合并成一个数组，然后求中间的数，但是时间复杂度是O(m+n)
* */
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        float res = 0;
        int len1 = nums1.length;
        int len2 = nums2.length;
        int i=0;
        int j = 0;
        int k = 0;
        int [] all = new int[len1 + len2];
        while( i < len1 && j < len2){
            if(nums1[i]< nums2[j]){
                all[k] = nums1[i];
                i++;
                k++;
            }
            else{
                all[k] = nums2[j];
                j++;
                k++;
            }
        }
        while( i < len1){
            all[k] = nums1[i];
            i++;
            k++;
        }
        while(j<len2){
            all[k] = nums2[j];
            k++;
            j++;
        }
        if((len1 + len2) % 2 ==0){
            int median = (len1 + len2) / 2;
            res = ((float)all[median] + (float)all[median-1]) / 2;
        }
        else{
            res = (float)all[(len1 + len2) / 2];
        }
        return res;
    }
}

/*
*
* */
class Solution2{
    public double findMedianSortedArrays(int[] nums1, int[] nums2){
        double res = 0;

        return res;
    }
}