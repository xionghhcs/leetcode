package contest103th;

public class P2 {
    public static void main(String[] args) {
        int[][] n = {{-1, -1, -1, -1, -1, -1},
                        {-1, -1, -1, -1, -1, -1},
                        {-1, -1, -1, -1, -1, -1},
                        {-1, 35, -1, -1, 13, -1},
                        {-1, -1, -1, -1, -1, -1},
                        {-1, 15, -1, -1, -1, -1}};
        int[][] n2 = {{-1,-1},{-1, 1}};
        Solution so = new Solution();

        System.out.println(so.snakesAndLadders(n2));
    }
}

class Solution {
    public int snakesAndLadders(int[][] board) {
        int row = board.length;
        int col = board[0].length;
        int start = 1;
        int cnt = 0;
        while (start != row * col) {
            int r = (start - 1) / row;
            r = row - r - 1;
            //判断方向
            int direction = 0;
            if (r % 2 == 0) {
                if (row % 2 == 0) {
                    direction = -1;
                } else {
                    direction = 1;
                }

            } else {
                if (row % 2 == 0) {
                    direction = 1;
                } else {
                    direction = -1;
                }
            }
            int c = (start - 1) % col;
            if(direction == -1){
                c = col - c - 1;
            }
            if (board[r][c] == -2){
                return -1;
            }
            else {
                board[r][c] = -2;
            }
            int n_r = r ;
            int n_c = c;
            if(n_c + direction >=col || n_c + direction < 0){
                n_r -= 1;
            }
            else{
                n_c += direction;
            }
            System.out.println("("+n_r+","+n_c+")");
            if(board[n_r][n_c] == -1){
                start = start + 1;
            }
            else{
                start = board[n_r][n_c];
            }
            cnt += 1;
        }
        return cnt - 1;
    }
}