package problem13;

public class Problem13 {
}

/*
* 暴力枚举
* */
class Solution {
    public int romanToInt(String s) {
        int res=0;
        s = " "+s;
        int j = s.length() -1;
        while(j>0){
            if (s.charAt(j) == ' '){
                break;
            }
            if(s.charAt(j)=='I'){
                res += 1;
            }
            else if(s.charAt(j) == 'V'){
                if(s.charAt(j-1) == 'I'){
                    res += 4;
                    j-=1;
                }
                else{
                    res += 5;
                }
            }
            else if(s.charAt(j) == 'X'){
                if(s.charAt(j-1) == 'I'){
                    res += 9;
                    j-=1;
                }
                else{
                    res += 10;
                }
            }
            else if(s.charAt(j) == 'L'){
                if(s.charAt(j-1) == 'X'){
                    res += 40;
                    j-=1;
                }
                else{
                    res += 50;
                }
            }
            else if(s.charAt(j) == 'C'){
                if(s.charAt(j-1) == 'X'){
                    res += 90;
                    j-=1;
                }
                else{
                    res += 100;
                }
            }
            else if(s.charAt(j) == 'D'){
                if(s.charAt(j-1) == 'C'){
                    res += 400;
                    j-=1;
                }
                else{
                    res += 500;
                }
            }
            else if(s.charAt(j) == 'M'){
                if(s.charAt(j-1) == 'C'){
                    res += 900;
                    j-=1;
                }
                else{
                    res += 1000;
                }
            }
            j-=1;
        }
        return res;
    }
}

/*
* 更优雅一点的方法
* */

class Solution2{
    public int romanToInt(String s) {
        int res = 0;
        return res;
    }

}