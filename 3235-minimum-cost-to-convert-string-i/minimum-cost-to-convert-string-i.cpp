class Solution {
public:
    long long minimumCost(string source, string target,
                          vector<char>& original,
                          vector<char>& changed,
                          vector<int>& cost) {
        
        const long long INF = 1e18;
        int n = 26;
        
        vector<vector<long long>> dist(n, vector<long long>(n, INF));
        
        // Distance to self = 0
        for (int i = 0; i < n; i++)
            dist[i][i] = 0;
        
        // Insert direct edges
        for (int i = 0; i < original.size(); i++) {
            int u = original[i] - 'a';
            int v = changed[i] - 'a';
            dist[u][v] = min(dist[u][v], (long long)cost[i]);
        }
        
        // Floyd–Warshall
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (dist[i][k] < INF && dist[k][j] < INF)
                        dist[i][j] = min(dist[i][j],
                                         dist[i][k] + dist[k][j]);
        
        long long total = 0;
        
        for (int i = 0; i < source.size(); i++) {
            int u = source[i] - 'a';
            int v = target[i] - 'a';
            
            if (dist[u][v] == INF)
                return -1;
            
            total += dist[u][v];
        }
        
        return total;
    }
};
