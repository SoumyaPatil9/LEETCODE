class Solution:
    def reverseBits(self, n):
        result = 0
        
        for _ in range(32):
            # Shift result left to make space
            result <<= 1
            
            # Add the last bit of n to result
            result |= (n & 1)
            
            # Shift n right to process next bit
            n >>= 1
        
        return result
