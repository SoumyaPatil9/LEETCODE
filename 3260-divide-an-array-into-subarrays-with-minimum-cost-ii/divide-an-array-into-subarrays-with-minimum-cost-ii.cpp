class Solution {
public:
    long long minimumCost(vector<int>& nums, int k, int dist) {
        int n = nums.size();
        int need = k - 1;
        long long ans = LLONG_MAX;

        multiset<long long> small, large;
        long long sumSmall = 0;

        int windowEnd = min(n - 1, dist + 1);

        // Initialize first window [1 .. windowEnd]
        for (int i = 1; i <= windowEnd; i++) {
            small.insert(nums[i]);
            sumSmall += nums[i];
        }

        // Keep only k-1 smallest in small
        while (small.size() > need) {
            auto it = prev(small.end());
            sumSmall -= *it;
            large.insert(*it);
            small.erase(it);
        }

        if (small.size() == need)
            ans = min(ans, nums[0] + sumSmall);

        // Slide window
        for (int start = 2; start + dist < n; start++) {

            int removeIdx = start - 1;
            int addIdx = start + dist;

            long long removeVal = nums[removeIdx];

            // Remove safely
            auto itSmall = small.find(removeVal);
            if (itSmall != small.end()) {
                sumSmall -= removeVal;
                small.erase(itSmall);
            } else {
                large.erase(large.find(removeVal));
            }

            // Add new element
            long long addVal = nums[addIdx];
            if (!small.empty() && addVal < *prev(small.end())) {
                small.insert(addVal);
                sumSmall += addVal;
            } else {
                large.insert(addVal);
            }

            // Rebalance
            while (small.size() > need) {
                auto it = prev(small.end());
                sumSmall -= *it;
                large.insert(*it);
                small.erase(it);
            }

            while (small.size() < need && !large.empty()) {
                auto it = large.begin();
                sumSmall += *it;
                small.insert(*it);
                large.erase(it);
            }

            if (small.size() == need)
                ans = min(ans, nums[0] + sumSmall);
        }

        return ans;
    }
};
