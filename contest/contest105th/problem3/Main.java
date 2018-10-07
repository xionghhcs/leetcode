package contest105th.problem3;

import java.util.*;

public class Main {
    public static void main(String[] args) {

    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */
class CBTInserter {
    private TreeNode r = null;

    public CBTInserter(TreeNode root) {
        r = root;
    }

    public int insert(int v) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(r);
        while(queue.size()>0) {
            TreeNode tmp_node = queue.poll();
            if(tmp_node.left == null) {
                tmp_node.left = new TreeNode(v);
                return tmp_node.val;
            }
            else if(tmp_node.right == null){
                tmp_node.right = new TreeNode(v);
                return tmp_node.val;
            }
            else {
                queue.add(tmp_node.left);
                queue.add(tmp_node.right);
            }
        }
        return 1;
    }

    public TreeNode get_root() {

        return r;
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.insert(v);
 * TreeNode param_2 = obj.get_root();
 */