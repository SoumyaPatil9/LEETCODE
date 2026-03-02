class Solution {
    public int numSteps(String s) {
        int steps = 0;
        int carry = 0;
        
        // Traverse from right to left (ignore first bit for now)
        for (int i = s.length() - 1; i > 0; i--) {
            int bit = s.charAt(i) - '0';
            
            if (bit + carry == 1) {
                // odd case
                steps += 2;  // add 1 + divide by 2
                carry = 1;
            } else {
                // even case
                steps += 1;  // just divide by 2
            }
        }
        
        // If carry remains, we need one extra step
        return steps + carry;
    }
}