/*
* 28. Implement strStr()
*
* Author : xionghh
*
* Date : 2018-04-29
* */
package problem28;

public class Problem28 {
}

/*
* 暴力，取出字串，然后比较是否相等
* */
class Solution {
    public int strStr(String haystack, String needle) {
        if(needle == ""){
            return 0;
        }
        if(haystack.length() < needle.length()){
            return -1;
        }
        int res = -1;
        int i = needle.length();
        int len = needle.length();
        for(;i<=haystack.length();i++){
            String sub = haystack.substring(i-len, i);
            System.out.println(sub);
            if(needle.equals(sub)){
                res = i-len;
                return res;
            }
        }
        return res;
    }
}