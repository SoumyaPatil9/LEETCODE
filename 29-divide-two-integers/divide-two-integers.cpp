class Solution {
public:
    int divide(int dividend, int divisor) {
        // Handle overflow
        if (dividend == INT_MIN && divisor == -1)
            return INT_MAX;
        
        // Determine sign
        bool negative = (dividend < 0) ^ (divisor < 0);
        
        long long dvd = labs((long long)dividend);
        long long dvs = labs((long long)divisor);
        long long result = 0;
        
        while (dvd >= dvs) {
            long long temp = dvs, multiple = 1;
            
            while (dvd >= (temp << 1)) {
                temp <<= 1;
                multiple <<= 1;
            }
            
            dvd -= temp;
            result += multiple;
        }
        
        if (negative)
            result = -result;
        
        return (int)result;
    }
};
