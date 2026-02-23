class Solution:
    def nextBeautifulNumber(self, n):
        
        # Function to check if a number is numerically balanced
        def isBalanced(x):
            freq = {}
            
            # Count digits
            for ch in str(x):
                digit = int(ch)
                if digit == 0:
                    return False
                freq[digit] = freq.get(digit, 0) + 1
            
            # Check condition: digit appears exactly digit times
            for digit in freq:
                if freq[digit] != digit:
                    return False
            
            return True
        
        num = n + 1
        
        while True:
            if isBalanced(num):
                return num
            num += 1