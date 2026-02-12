class Solution {
public:
    void inorder(TreeNode* root, vector<int>& vals) {
        if (!root) return;
        inorder(root->left, vals);
        vals.push_back(root->val);
        inorder(root->right, vals);
    }
    
    TreeNode* buildBalanced(vector<int>& vals, int left, int right) {
        if (left > right) return NULL;
        
        int mid = left + (right - left) / 2;
        
        TreeNode* root = new TreeNode(vals[mid]);
        root->left = buildBalanced(vals, left, mid - 1);
        root->right = buildBalanced(vals, mid + 1, right);
        
        return root;
    }
    
    TreeNode* balanceBST(TreeNode* root) {
        vector<int> vals;
        inorder(root, vals);
        return buildBalanced(vals, 0, vals.size() - 1);
    }
};
