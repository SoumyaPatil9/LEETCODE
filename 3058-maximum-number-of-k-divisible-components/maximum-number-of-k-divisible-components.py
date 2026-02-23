from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k):
        # Build adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        self.count = 0  # Number of valid components
        
        def dfs(node, parent):
            total = values[node]
            for nei in graph[node]:
                if nei == parent:
                    continue
                total += dfs(nei, node)
            
            if total % k == 0:
                self.count += 1
                return 0  # Cut this subtree
            return total
        
        dfs(0, -1)
        return self.count


# Example usage:
sol = Solution()
n = 5
edges = [[0,2],[1,2],[1,3],[2,4]]
values = [1,8,1,4,4]
k = 6
print(sol.maxKDivisibleComponents(n, edges, values, k))  # Output: 2