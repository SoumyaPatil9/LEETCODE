class Solution {
public:
    int minCost(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();

        const long long INF = LLONG_MAX / 4;

        vector dist(m, vector(n, vector<long long>(k+1, INF)));

        using T = tuple<long long,int,int,int>;
        priority_queue<T, vector<T>, greater<T>> pq;

        dist[0][0][0] = 0;
        pq.push({0, 0, 0, 0});

        // Flatten and sort cells
        vector<tuple<int,int,int>> cells;
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                cells.push_back({grid[i][j], i, j});

        sort(cells.begin(), cells.end());

        // pointer per teleport layer
        vector<int> ptr(k+1, 0);

        while(!pq.empty()) {
            auto [cost, r, c, t] = pq.top();
            pq.pop();

            if(cost > dist[r][c][t]) continue;

            if(r == m-1 && c == n-1)
                return cost;

            // normal moves
            if(r+1 < m) {
                long long nc = cost + grid[r+1][c];
                if(nc < dist[r+1][c][t]) {
                    dist[r+1][c][t] = nc;
                    pq.push({nc, r+1, c, t});
                }
            }

            if(c+1 < n) {
                long long nc = cost + grid[r][c+1];
                if(nc < dist[r][c+1][t]) {
                    dist[r][c+1][t] = nc;
                    pq.push({nc, r, c+1, t});
                }
            }

            // teleport
            if(t < k) {
                int currVal = grid[r][c];

                while(ptr[t] < cells.size() &&
                      get<0>(cells[ptr[t]]) <= currVal) {

                    auto [val, x, y] = cells[ptr[t]];
                    ptr[t]++;

                    if(cost < dist[x][y][t+1]) {
                        dist[x][y][t+1] = cost;
                        pq.push({cost, x, y, t+1});
                    }
                }
            }
        }

        return -1;
    }
};
