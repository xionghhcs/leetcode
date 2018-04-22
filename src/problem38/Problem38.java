/*
* 38. Count and Say
*
* Author : xionghh
*
* Date : 2018-04-22
* */

package problem38;

public class Problem38 {
}

class Solution {
    public String countAndSay(int n) {
        String res = "1";
        if(n == 1){
            return res;
        }
        for(int i=0;i<n-1;i++){
            String tmp = "";
            res += 5;
            char pre_c = res.charAt(0);
            int num = 0;
            for(int j=0;j<res.length();j++){
                char c = res.charAt(j);
                if(c == pre_c){
                    num ++;
                }
                else{
                    tmp += String.valueOf(num);
                    tmp += pre_c;
                    num = 1;
                    pre_c = c;
                }
            }
            res = tmp;
        }
        return res;
    }
}