#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximizeSquareHoleArea(int n, int m, vector<int>& hBars, vector<int>& vBars) {
        const int MOD = 1e9 + 7;

        sort(hBars.begin(), hBars.end());
        sort(vBars.begin(), vBars.end());

        int maxH = 1, maxV = 1;

        // Longest consecutive horizontal bars
        int count = 1;
        for (int i = 1; i < hBars.size(); i++) {
            if (hBars[i] == hBars[i - 1] + 1) {
                count++;
            } else {
                maxH = max(maxH, count + 1);
                count = 1;
            }
        }
        maxH = max(maxH, count + 1);

        // Longest consecutive vertical bars
        count = 1;
        for (int i = 1; i < vBars.size(); i++) {
            if (vBars[i] == vBars[i - 1] + 1) {
                count++;
            } else {
                maxV = max(maxV, count + 1);
                count = 1;
            }
        }
        maxV = max(maxV, count + 1);

        long long side = min(maxH, maxV);
        return (side * side) % MOD;
    }
};
