class Solution {
    public int myAtoi(String s) {
        int i = 0, n = s.length();
        
        // 1. Skip leading spaces
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }
        
        // If string is empty after removing spaces
        if (i == n) return 0;
        
        // 2. Check sign
        int sign = 1;
        if (s.charAt(i) == '+' || s.charAt(i) == '-') {
            sign = (s.charAt(i) == '-') ? -1 : 1;
            i++;
        }
        
        long result = 0;  // use long to detect overflow
        
        // 3. Convert digits
        while (i < n && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';
            
            result = result * 10 + digit;
            
            // 4. Handle overflow immediately
            if (sign * result >= Integer.MAX_VALUE)
                return Integer.MAX_VALUE;
            if (sign * result <= Integer.MIN_VALUE)
                return Integer.MIN_VALUE;
            
            i++;
        }
        
        return (int)(sign * result);
    }
}
