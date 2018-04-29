/*
* 88. Merge Sorted Array
*
* Author : xionghh
*
* Date : 2018-04-29
* */
package problem88;

public class Problem88 {
}

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int [] res = new int[m+n];
        int i=0;
        int j=0;
        int res_idx = 0;
        while(i<m && j<n){
            if(nums1[i]<nums2[j]){
                res[res_idx++] = nums1[i];
                i++;
            }
            else{
                res[res_idx++] =nums2[j];
                j++;
            }
        }
        while(i<m){
            res[res_idx++] = nums1[i++];
        }
        while(j<n) res[res_idx++] = nums2[j++];
        System.arraycopy(res,0,nums1,0,res.length);
    }
}

