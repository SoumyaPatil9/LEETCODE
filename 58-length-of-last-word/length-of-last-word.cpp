class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.length();
        int length = 0;
        int i = n - 1;
        
        // Step 1: Skip trailing spaces
        while (i >= 0 && s[i] == ' ') {
            i--;
        }
        
        // Step 2: Count last word length
        while (i >= 0 && s[i] != ' ') {
            length++;
            i--;
        }
        
        return length;
    }
};
