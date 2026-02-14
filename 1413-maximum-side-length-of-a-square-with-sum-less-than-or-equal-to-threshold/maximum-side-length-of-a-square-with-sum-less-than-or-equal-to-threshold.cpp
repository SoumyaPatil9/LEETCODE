class Solution {
public:
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
        int m = mat.size();
        int n = mat[0].size();
        
        // Step 1: Compute prefix sum
        vector<vector<int>> psum(m+1, vector<int>(n+1, 0));
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                psum[i+1][j+1] = mat[i][j] + psum[i][j+1] + psum[i+1][j] - psum[i][j];
            }
        }
        
        // Step 2: Binary search on side length
        int left = 0, right = min(m,n), ans = 0;
        
        while(left <= right) {
            int mid = left + (right - left) / 2;
            bool found = false;
            
            for(int i = mid; i <= m && !found; i++) {
                for(int j = mid; j <= n && !found; j++) {
                    int total = psum[i][j] - psum[i-mid][j] - psum[i][j-mid] + psum[i-mid][j-mid];
                    if(total <= threshold) found = true;
                }
            }
            
            if(found) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return ans;
    }
};
