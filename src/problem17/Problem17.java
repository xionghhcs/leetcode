/*
* 17. Letter Combinations of a Phone Number
*
* Author : xionghh
*
* Date : 2018-04-06
* */

package problem17;

import java.util.*;

public class Problem17 {
    public static void main(String[] args) {
        String digits = "123";
        Solution so = new Solution();
        so.letterCombinations(digits);
    }
}

class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        if(digits.equals("")){
            return res;
        }
        Map<Character, String[]> digit2char = new HashMap<Character, String[]>();
        digit2char.put('2',new String[]{"a","b","c"});
        digit2char.put('3',new String[]{"d","e","f"});
        digit2char.put('4',new String[]{"g","h","i"});
        digit2char.put('5',new String[]{"j","k","l"});
        digit2char.put('6',new String[]{"m","n","o"});
        digit2char.put('7',new String[]{"p","q","r","s"});
        digit2char.put('8',new String[]{"t","u","v"});
        digit2char.put('9',new String[]{"w","x","y","z"});
        res.add("");
        for(int i=0;i<digits.length();i++){
            char c = digits.charAt(i);
            String [] s = digit2char.get(c);
            int res_len = res.size();
            for(int j = 0;j<res_len;j++){
                String cur_s = res.get(j);
                for(String cc:s){
                    res.add(cur_s + cc);
                }
            }
            res = res.subList(res_len, res.size());
        }
        return res;
    }
}
