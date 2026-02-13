class Solution {
public:
    long long maxSumTrionic(vector<int>& nums) {
        int n = nums.size();
        const long long NEG = -4e18;

        vector<long long> up(n, NEG);
        vector<long long> down(n, NEG);
        vector<long long> tri(n, NEG);

        long long ans = NEG;

        for (int i = 1; i < n; i++) {

            // ---- Phase 1: Increasing ----
            if (nums[i] > nums[i-1]) {
                up[i] = max(
                    up[i-1] != NEG ? up[i-1] + nums[i] : NEG,
                    (long long)nums[i-1] + nums[i]
                );
            }

            // ---- Phase 2: Decreasing ----
            if (nums[i] < nums[i-1]) {

                // Start decreasing from valid increasing
                if (up[i-1] != NEG)
                    down[i] = up[i-1] + nums[i];

                // Continue decreasing
                if (down[i-1] != NEG)
                    down[i] = max(down[i], down[i-1] + nums[i]);
            }

            // ---- Phase 3: Final Increasing ----
            if (nums[i] > nums[i-1]) {

                // Start final increase
                if (down[i-1] != NEG)
                    tri[i] = down[i-1] + nums[i];

                // Continue final increase
                if (tri[i-1] != NEG)
                    tri[i] = max(tri[i], tri[i-1] + nums[i]);
            }

            ans = max(ans, tri[i]);
        }

        return ans;
    }
};
