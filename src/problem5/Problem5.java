/*
 * 5. Longest Palindromic Substring
 *
 * Author : xionghh
 *
 * Date : 2018-04-10
 * */

package problem5;

public class Problem5 {
    public static void main(String[] args) {

    }
}

/*
 * 暴力:
 * 遍历所有的字串，并判断每个字串是否是回文的
 *
 * */
class Solution {
    public String longestPalindrome(String s) {
        if (s.length() == 1 || s.length() == 0) {
            return s;
        }
        int max_len = 1;
        int max_i = 0;
        int max_j = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                if (checkPalindome(s, i, j) && (j - i + 1) > max_len) {
                    max_len = j - i + 1;
                    max_i = i;
                    max_j = j;
                }
            }
        }
        return s.substring(max_i, max_j);
    }

    boolean checkPalindome(String s, int i, int j) {
        boolean flag = false;
        while (i <= j) {
            if (s.charAt(i) != s.charAt(j)) {
                break;
            }
            i++;
            j--;
        }
        if (i > j) {
            flag = true;

        } else {
            flag = false;
        }
        return flag;
    }
}

/*
*
*
* */
class Solution2 {
    public String longestPalindrome(String s) {
        String res = "";
        for (int i = 0; i < s.length(); i++) {
            String tmp = checkPalindrom(s, i);
            if (tmp.length() > res.length()) {
                res = tmp;
            }
        }
        return res;
    }

    String checkPalindrom(String s, int center) {

        // if (center == 0 || center == s.length()-1) {
        //     return String.valueOf(s.charAt(center));
        // }
        int i = center;
        int j = center;
        String odd_str = "";
        while (i >= 0 && j < s.length() && s.charAt(i) == s.charAt(j)) {
            i--;
            j++;
        }
        i++;
        j--;
        odd_str = s.substring(i, j+1);

        i = center - 1;
        j = center;
        while (i >= 0 && j < s.length() && s.charAt(i) == s.charAt(j)) {
            i--;
            j++;
        }
        i++;
        j--;
        String even_str = "";
        if(i<=j){
            even_str = s.substring(i,j+1);
        }
        // System.out.println(center+":"+even_str+":"+odd_str);
        if (even_str.length() > odd_str.length()) {
            return even_str;
        } else {
            return odd_str;
        }

    }
}

/*
* 线性时间解法
*
* */
class Solution3{
    public String longestPalindrome(String s) {
        String res = "";

        return res;
    }
}
