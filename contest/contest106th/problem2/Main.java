package contest106th.problem2;

import java.util.Stack;

public class Main {
}

class Solution {
    public int minAddToMakeValid(String S) {
        int res = 0;
        Stack<Character> s = new Stack<>();
        int i = 0;
        while (i < S.length()) {
            Character c = S.charAt(i);
            i += 1;
            if (s.empty()) {
                s.push(c);
            } else {
                Character top = s.peek();
                if(top == '(' && c== ')'){
                    s.pop();
                }
                else{
                    s.push(c);
                }
            }
        }
        res = s.size();
        return res;
    }
}
