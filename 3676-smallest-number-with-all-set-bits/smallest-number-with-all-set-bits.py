class Solution:
    def smallestNumber(self, n):
        k = n.bit_length()
        return (1 << k) - 1