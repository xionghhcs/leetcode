package contest106th.problem3;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {
}

/*
* TLE
* */
class Solution {
    public int threeSumMulti(int[] A, int target) {
        Arrays.sort(A);
        int res = 0;
        for(int i =0;i<A.length; i++){
            if (A[i] > target){
                break;
            }
            for(int j=1;j<A.length;j++){
                if(A[i] + A[j] > target){
                    break;
                }
                for(int k=2;k<A.length;k++){
                    if(A[i]+ A[j] + A[k] > target){
                        break;
                    }
                    if(A[i] + A[j] + A[k] == target){
                        res += 1;
                         res = res % (1000000000 + 7);
                    }
                }
            }
        }
        return res;
    }
}


class Solution2 {
    public int threeSumMulti(int[] A, int target) {
        Map map = new HashMap<Integer, Integer>();
        Integer ans = 0;
        int mod = 1000000007;
        for(int i =0;i<A.length;i++){
            for(int j=0;j<A.length;j++){
                int t = target - A[i] - A[j];
                ans = (ans + (int)map.getOrDefault(t, 0) ) % mod ;
            }
            int v = (int)map.getOrDefault(A[i], 0);
            v += 1;
            map.put(Integer.valueOf(A[i]), Integer.valueOf(v));
        }
        return (int)ans;
    }
}

class Solution3{
    /*
    * @author : zhantons(leetcode id)
    *
    * There is not necessary to sort the array of A
    * */
    public int threeSumMulti(int[] A, int target) {
        int ans = 0;
        int mod = 1000000007;
        for(int i=0;i<A.length; i++){
            HashMap<Integer, Integer> map = new HashMap<>();
            map.put(A[A.length - 1], 1);
            for(int j= A.length - 2; j > i; j--){
                ans = (ans + map.getOrDefault(target - A[i] - A[j], 0)) % mod;
                map.put(A[j], map.getOrDefault(A[j], 0) + 1);
            }
        }
        return ans;
    }
}

class Solution4{
    /*
    * @Author: 	szp14
    *
    * DP
    * */
    private int [][] dp;
    public int threeSumMulti(int[] A, int target) {
        int ans = 0;
        int mod = 1000000007;
        dp = new int[3][305];
        for(int i=0;i<A.length;i++){
            for(int j=2;j>=1;j--){
                for(int k=target; k>=A[i]; k--){
                    dp[j][k] = (dp[j][k] + dp[j -1][k - A[i]]) % mod;
                }
            }
            dp[0][A[i]] = (dp[0][A[i]] + 1) % mod;
        }
        return ans;
    }
}