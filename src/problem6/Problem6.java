/*
* 6. ZigZag Conversion
*
* Author : xionghh
*
* Date : 2018-04-08
* */
package problem6;

public class Problem6 {

}

class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1){
            return s;
        }
        String[] rows = new String[numRows];
        for(int i =0;i<rows.length;i++){
            rows[i] = "";
        }
        int i = 0;
        int flag = 1;
        for (int j = 0; j < s.length(); j++) {
            char c = s.charAt(j);
            rows[i] += c;
            if(i == numRows -1){
                flag = -1;
            }
            else if(i == 0){
                flag = 1;
            }
            i += flag;
        }
        String res = "";
        for (String row : rows) {
            System.out.println(row);
            res += row;
        }
        return res;
    }
}
