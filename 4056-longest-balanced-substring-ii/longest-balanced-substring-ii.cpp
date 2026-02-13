class Solution {
public:
    int longestBalanced(string s) {
        int n = s.size();
        int ans = 1;  // at least 1 character is always balanced

        // -----------------------------
        // Case 1: single character runs
        // -----------------------------
        int cnt = 1;
        for (int i = 1; i < n; i++) {
            if (s[i] == s[i-1]) cnt++;
            else cnt = 1;
            ans = max(ans, cnt);
        }

        // -----------------------------
        // Case 2: subsets of size >= 2
        // -----------------------------
        for (int mask = 1; mask < 8; mask++) {

            // skip single character masks
            if (mask == 1 || mask == 2 || mask == 4) continue;

            unordered_map<long long,int> first;
            first[0] = -1;

            int a = 0, b = 0, c = 0;

            for (int i = 0; i < n; i++) {

                char ch = s[i];

                // if char not allowed in this subset → reset
                if ((ch == 'a' && !(mask & 1)) ||
                    (ch == 'b' && !(mask & 2)) ||
                    (ch == 'c' && !(mask & 4))) {

                    first.clear();
                    first[0] = i;
                    a = b = c = 0;
                    continue;
                }

                if (ch == 'a') a++;
                if (ch == 'b') b++;
                if (ch == 'c') c++;

                long long key;

                if (mask == 3) key = a - b;       // a,b
                else if (mask == 5) key = a - c;  // a,c
                else if (mask == 6) key = b - c;  // b,c
                else key = ((long long)(a - b) << 32) ^ (a - c); // a,b,c

                if (first.count(key))
                    ans = max(ans, i - first[key]);
                else
                    first[key] = i;
            }
        }

        return ans;
    }
};
