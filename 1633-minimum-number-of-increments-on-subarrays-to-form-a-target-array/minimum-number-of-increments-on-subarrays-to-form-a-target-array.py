class Solution:
    def minNumberOperations(self, target):
        n = len(target)
        
        # First element must be built from 0
        operations = target[0]
        
        # Add only positive increases from previous element
        for i in range(1, n):
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
        
        return operations


# Example usage:
sol = Solution()

print(sol.minNumberOperations([1,2,3,2,1]))  # Output: 3
print(sol.minNumberOperations([3,1,1,2]))    # Output: 4
print(sol.minNumberOperations([3,1,5,4,2]))  # Output: 7