class Solution {
public:
    long long minimumCost(string source, string target,
                          vector<string>& original,
                          vector<string>& changed,
                          vector<int>& cost) {
        
        int n = source.length();
        const long long INF = 1e18;

        // Step 1: Collect unique strings
        unordered_map<string, int> id;
        int idx = 0;

        for (auto &s : original)
            if (!id.count(s)) id[s] = idx++;

        for (auto &s : changed)
            if (!id.count(s)) id[s] = idx++;

        int m = idx;

        vector<vector<long long>> dist(m, vector<long long>(m, INF));
        for (int i = 0; i < m; i++)
            dist[i][i] = 0;

        for (int i = 0; i < original.size(); i++) {
            int u = id[original[i]];
            int v = id[changed[i]];
            dist[u][v] = min(dist[u][v], (long long)cost[i]);
        }

        // Floyd-Warshall
        for (int k = 0; k < m; k++)
            for (int i = 0; i < m; i++)
                for (int j = 0; j < m; j++)
                    if (dist[i][k] < INF && dist[k][j] < INF)
                        dist[i][j] = min(dist[i][j],
                                         dist[i][k] + dist[k][j]);

        // Group lengths
        unordered_set<int> lengths;
        for (auto &s : original)
            lengths.insert(s.length());

        vector<long long> dp(n + 1, INF);
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            if (dp[i] == INF) continue;

            // Case 1: single character match
            if (source[i] == target[i])
                dp[i + 1] = min(dp[i + 1], dp[i]);

            // Case 2: try valid lengths only
            for (int len : lengths) {
                if (i + len > n) continue;

                string s = source.substr(i, len);
                string t = target.substr(i, len);

                if (!id.count(s) || !id.count(t)) continue;

                int u = id[s];
                int v = id[t];

                if (dist[u][v] < INF)
                    dp[i + len] = min(dp[i + len],
                                      dp[i] + dist[u][v]);
            }
        }

        return dp[n] == INF ? -1 : dp[n];
    }
};
