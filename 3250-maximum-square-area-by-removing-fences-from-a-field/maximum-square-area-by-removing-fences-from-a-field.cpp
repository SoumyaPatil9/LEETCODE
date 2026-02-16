#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximizeSquareArea(int m, int n, vector<int>& hFences, vector<int>& vFences) {
        const int MOD = 1e9 + 7;

        // Add borders
        hFences.push_back(1);
        hFences.push_back(m);
        vFences.push_back(1);
        vFences.push_back(n);

        sort(hFences.begin(), hFences.end());
        sort(vFences.begin(), vFences.end());

        // Store all possible horizontal distances
        unordered_set<int> hDist;
        for (int i = 0; i < hFences.size(); i++) {
            for (int j = i + 1; j < hFences.size(); j++) {
                hDist.insert(hFences[j] - hFences[i]);
            }
        }

        long long maxSide = 0;

        // Check vertical distances and match with horizontal ones
        for (int i = 0; i < vFences.size(); i++) {
            for (int j = i + 1; j < vFences.size(); j++) {
                int dist = vFences[j] - vFences[i];
                if (hDist.count(dist)) {
                    maxSide = max(maxSide, (long long)dist);
                }
            }
        }

        if (maxSide == 0) return -1;

        return (maxSide * maxSide) % MOD;
    }
};
