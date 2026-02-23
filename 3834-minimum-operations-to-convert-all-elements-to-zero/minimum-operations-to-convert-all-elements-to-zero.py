class Solution:
    def minOperations(self, nums):
        stack = []
        operations = 0
        
        for num in nums:
            # Remove larger elements (since smaller ones get removed first)
            while stack and stack[-1] > num:
                stack.pop()
            
            # If new positive layer starts
            if num > 0 and (not stack or stack[-1] < num):
                operations += 1
                stack.append(num)
        
        return operations