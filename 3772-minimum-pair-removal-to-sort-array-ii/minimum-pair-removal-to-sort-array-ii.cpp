class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        vector<long long> val(nums.begin(), nums.end());
        vector<int> prev(n), next(n);
        vector<bool> alive(n, true);

        for (int i = 0; i < n; i++) {
            prev[i] = i - 1;
            next[i] = (i + 1 < n ? i + 1 : -1);
        }

        // Count decreasing positions
        int bad = 0;
        for (int i = 0; i + 1 < n; i++) {
            if (val[i] > val[i + 1]) bad++;
        }

        if (bad == 0) return 0;

        // Min heap: {sum, index}
        priority_queue<
            pair<long long,int>,
            vector<pair<long long,int>>,
            greater<pair<long long,int>>
        > pq;

        for (int i = 0; i + 1 < n; i++) {
            pq.push({val[i] + val[i + 1], i});
        }

        int operations = 0;

        while (bad > 0) {
            auto [sum, i] = pq.top();
            pq.pop();

            if (!alive[i]) continue;
            int j = next[i];
            if (j == -1 || !alive[j]) continue;

            if (val[i] + val[j] != sum) continue;

            // Remove old bad relations
            int p = prev[i];
            int nj = next[j];

            if (p != -1 && val[p] > val[i]) bad--;
            if (val[i] > val[j]) bad--;
            if (nj != -1 && val[j] > val[nj]) bad--;

            // Merge
            val[i] = sum;
            alive[j] = false;

            next[i] = nj;
            if (nj != -1) prev[nj] = i;

            // Add new bad relations
            if (p != -1 && val[p] > val[i]) bad++;
            if (nj != -1 && val[i] > val[nj]) bad++;

            // Push new pairs to heap
            if (p != -1)
                pq.push({val[p] + val[i], p});
            if (nj != -1)
                pq.push({val[i] + val[nj], i});

            operations++;
        }

        return operations;
    }
};
