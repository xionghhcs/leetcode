/*
* 14. Longest Common Prefix
*
* Author : xionghh
*
* Date : 2018-04-07
* */
package problem14;

public class Problem14 {
}

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        } else if (strs.length == 1) {
            return strs[0];
        }
        String res = "";
        int min_len = Integer.MAX_VALUE;
        for (String str : strs) {
            if (str.length() < min_len) {
                min_len = str.length();
            }
        }
        for (int i = 0; i < min_len; i++) {
            boolean flag = false;
            for (int j = 1; j < strs.length; j++) {
                if(strs[j].charAt(i) != strs[0].charAt(i)){
                    flag = true;
                    break;
                }
            }
            if (flag) {
                break;
            }
            else{
                res += strs[0].charAt(i);
            }
        }
        return res;
    }
}