package contest106th.problem1;

public class Main {
    public static void main(String[] args) {
        Solution so = new Solution();
        int [] test  = {4,2,5,7};
        System.out.println(so.sortArrayByParityII(test));
    }
}

class Solution{
    public int[] sortArrayByParityII(int[] A) {
        int i=0;
        int j=0;
        int[] result = new int[A.length];
        for(int k=0;k<A.length;k++){
            if(k % 2 == 0){
                while (i < A.length){
                    if(A[i] % 2 ==0){
                        result[k] = A[i];
                        i++;
                        break;
                    }
                    else{
                        i++;
                    }
                }
            }
            else{
                while(j < A.length){
                    if(A[j] % 2 == 1){
                        result[k] = A[j];
                        j++;
                        break;
                    }
                    else{
                        j++;
                    }
                }
            }
        }
        return result;
    }
}

