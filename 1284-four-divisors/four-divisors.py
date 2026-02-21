class Solution:
    def sumFourDivisors(self, nums):
        def get_divisor_sum(n):
            count = 0
            total = 0
            
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    other = n // i
                    
                    if i == other:
                        count += 1
                        total += i
                    else:
                        count += 2
                        total += i + other
                    
                    if count > 4:
                        return 0
            
            return total if count == 4 else 0
        
        result = 0
        for num in nums:
            result += get_divisor_sum(num)
        
        return result