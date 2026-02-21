class Solution:
    def countTriples(self, n):
        count = 0
        
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_square = a * a + b * b
                c = int(c_square ** 0.5)
                
                if c <= n and c * c == c_square:
                    count += 1
        
        return count