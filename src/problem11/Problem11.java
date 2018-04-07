/*
* 11. Container With Most Water
*
* Author : xionghh
*
* Date : 2018-04-07
* */
package problem11;

public class Problem11 {
}

/*
* 暴力解法，当然碰到数据量大的时候就超时了n^2.
* */
class Solution {
    public int maxArea(int[] height) {
        int res = 0;
        for(int i=0;i<height.length;i++){
            for(int j=i+1;j<height.length;j++){
                if(Math.min(height[i], height[j]) * (j-i) > res){
                    res = Math.min(height[i], height[j]) * (j-i);
                }
            }
        }
        return res;
    }
}

/*
* 线性时间解法
* */
class Solution2 {
    public int maxArea(int[] height) {
        int res = 0;
        int i=0;
        int j= height.length-1;
        while(i<j){
            res = Math.max(res, Math.min(height[i], height[j]) * ( j-i));
            if(height[i]<height[j]){
                i++;
            }
            else{
                j--;
            }
        }
        return res;
    }
}
