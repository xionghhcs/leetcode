/*
* 29. Divide Two Integers
*
* Author : xionghh
*
* Date : 2018-04-29
* */
package problem29;

public class Problem29 {
    public static void main(String[] args) {
        System.out.println(1^0);
        System.out.println(Integer.MAX_VALUE);
    }
}

/*
*
* */
class Solution {
    public int divide(int dividend, int divisor) {
        if(dividend == Integer.MIN_VALUE && divisor == -1){
            return Integer.MAX_VALUE;
        }
        int sign = ((dividend<0)^(divisor<0))?-1:1;
        int res = 0;
        long dividend_l = Math.abs((long)dividend);
        long divisor_l = Math.abs((long)divisor);
        while(dividend_l >= divisor_l){
            int shiftnum = 0;
            while(dividend_l >= (divisor_l << shiftnum)){
                shiftnum ++;
            }
            res += 1<<(shiftnum-1);
            dividend_l -= divisor_l<<(shiftnum-1);
        }
        return sign * res;
    }
}