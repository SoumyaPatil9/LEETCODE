class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        
        sorted_pairs = [False] * (n - 1)
        deletions = 0
        
        for col in range(m):
            # Check if this column breaks order
            should_delete = False
            
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] > strs[i+1][col]:
                    should_delete = True
                    break
            
            if should_delete:
                deletions += 1
            else:
                # Update sorted status
                for i in range(n - 1):
                    if strs[i][col] < strs[i+1][col]:
                        sorted_pairs[i] = True
        
        return deletions