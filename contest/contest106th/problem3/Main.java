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
        System.out.println(A);
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
                        // res = res % (1000000000 + 7);
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