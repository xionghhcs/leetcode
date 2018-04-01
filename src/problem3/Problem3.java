package problem3;/*
* leetcode 3. Longest Substring Without Repeating Characters
*
* Author : xionghh
*
* Date : 2018-04-01
* */

import java.util.*;

public class Problem3 {
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        String s = "abcabcbb";
        Solution so = new Solution();
        System.out.println(so.lengthOfLongestSubstring(s));
    }
}

/*
* 直接暴力求解
* */
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max_len = 0;
        int s_len = s.length();
        for (int i = 0; i < s_len; i++) {
            char[] hash_table = new char[255];
            for (int k = 0; k < 255; k++) {
                hash_table[k] = 0;
            }
            int j = i;
            for (; j < s_len; j++) {
                if (hash_table[s.charAt(j)] > 0) {
                    break;
                } else {
                    hash_table[s.charAt(j)] = 1;
                }
            }
            if (j - i > max_len) {
                max_len = j - i;
            }
        }
        return max_len;
    }
}

/*
* 动态规划的方法
* */
class Solution1 {
    public int lengthOfLongestSubstring(String s) {
        int max_length = 0;

        return max_length;
    }
}