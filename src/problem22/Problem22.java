/*
* 22. Generate Parentheses
*
* Author : xionghh
*
* Date : 2018-04-29
* */

package problem22;

import java.util.ArrayList;
import java.util.List;

public class Problem22 {
}

/*
* 递归
* */
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        generate(n,n,"", res);
        return res;
    }

    void generate(int left, int right, String str, List<String> res) {
        if (left < 0 || right < 0 || left > right) {
            return;
        }
        if (left == 0 && right == 0) {
            res.add(str);
            return;
        }
        generate(left - 1, right, str + "(", res);
        generate(left, right - 1, str + ")", res);
    }
}

/*
*
* */
class Solution2 {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();

        return res;
    }

}