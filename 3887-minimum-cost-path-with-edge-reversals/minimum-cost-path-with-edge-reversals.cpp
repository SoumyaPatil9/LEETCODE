class Solution {
public:
    int minCost(int n, vector<vector<int>>& edges) {

        vector<vector<pair<int,int>>> adj(n);
        vector<vector<pair<int,int>>> incoming(n);

        for(auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            incoming[v].push_back({u, w});
        }

        const long long INF = LLONG_MAX / 4;
        vector<long long> dist(n, INF);

        using T = pair<long long,int>;
        priority_queue<T, vector<T>, greater<T>> pq;

        dist[0] = 0;
        pq.push({0, 0});

        while(!pq.empty()) {
            auto [cost, u] = pq.top();
            pq.pop();

            if(cost > dist[u]) continue;
            if(u == n-1) return cost;

            // Normal edges
            for(auto &[v, w] : adj[u]) {
                if(cost + w < dist[v]) {
                    dist[v] = cost + w;
                    pq.push({dist[v], v});
                }
            }

            // Reverse edges
            for(auto &[v, w] : incoming[u]) {
                long long newCost = cost + 2LL * w;
                if(newCost < dist[v]) {
                    dist[v] = newCost;
                    pq.push({newCost, v});
                }
            }
        }

        return -1;
    }
};
