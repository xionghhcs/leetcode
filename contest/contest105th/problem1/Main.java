package contest105th.problem1;

public class Main {
    public static void main(String[] args) {
        String test = "a-bC-dEf-ghIj";
        Solution so = new Solution();
        System.out.println(so.reverseOnlyLetters(test));
    }
}

class Solution {
    public String reverseOnlyLetters(String S) {
        String res = "";
        String reverse_s = new StringBuffer(S).reverse().toString();
        int j = 0;
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            if (S.charAt(i) >= 'A' && S.charAt(i) <= 'Z' || S.charAt(i) >= 'a' && S.charAt(i) <= 'z') {
                for (int j_index = j; j_index < reverse_s.length(); j_index += 1) {
                    char r = reverse_s.charAt(j_index);
                    if (r >= 'A' && r <= 'Z' || r >= 'a' && r <= 'z') {
                        res += r;
                        j = j_index + 1;
                        break;
                    }
                }
            } else {
                res += c;
            }
        }
        return res;
    }
}
