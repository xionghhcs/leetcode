package problem15;

import java.util.*;

public class Problem15 {
    public static void main(String[] args) {
        int[] nums = new int[]{-1, 0, 1, 2, -1, -4};
        Solution so = new Solution();
        so.threeSum(nums);
    }
}

/*
* 解法一：遍历每一对数字，然后在剩下的数里面查找是否有一个数可以使得这三个数和为0；很暴力。
* 又因为用到了set来去重，所以非常耗时
* */
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> res = new HashSet<>();
        Arrays.sort(nums);
        int i = 0;
        int j = nums.length - 1;
        for (; i < nums.length; i++) {
            j = nums.length - 1;
            for (; j > i + 1; j--) {
                int sum = nums[i] + nums[j];
                int val = -sum;
                int mid = binary_search(nums, i + 1, j - 1, val);
                if (mid != -1) {
                    List<Integer> tmp = new ArrayList<>();
                    tmp.add(nums[i]);
                    tmp.add(nums[mid]);
                    tmp.add(nums[j]);
                    res.add(tmp);
                }
            }
        }
        List list = new ArrayList(res);
        return list;
    }
    /*
    * 在下标区间i-j内进行二分查找
    * */
    public int binary_search(int[] nums, int i, int j, int val) {
        if (i > j) {
            return -1;
        }
        int mid = (i + j) / 2;
        if (nums[mid] == val) {
            return mid;
        } else if (nums[mid] < val) {
            return binary_search(nums, mid + 1, j, val);
        } else {
            return binary_search(nums, i, mid - 1, val);
        }
    }
}

class Solution2 {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        int i = 0;
        for (; i < nums.length; i++) {
            if (nums[i] > 0) {
                break;
            }
            if(i>0 && nums[i] == nums[i-1]){
                continue;
            }
            int j = i + 1;
            int k = nums.length - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    List<Integer> tmp = new ArrayList<>();
                    tmp.add(nums[i]);
                    tmp.add(nums[j]);
                    tmp.add(nums[k]);
                    res.add(tmp);
                    int tmpj = nums[j];
                    int tmpk = nums[k];
                    while(j<k && nums[j] == tmpj) j++;
                    while(j<k && nums[k] == tmpk) k--;
                    if(j>=k) break;
                } else if (sum < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }
        return res;
    }
}
