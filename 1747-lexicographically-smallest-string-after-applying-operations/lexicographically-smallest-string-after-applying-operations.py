from collections import deque

class Solution:
    def findLexSmallestString(self, s, a, b):
        visited = set()
        queue = deque([s])
        visited.add(s)
        
        smallest = s
        
        while queue:
            curr = queue.popleft()
            if curr < smallest:
                smallest = curr
            
            # Operation 1: Add 'a' to odd indices
            arr = list(curr)
            for i in range(1, len(arr), 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            add_op = "".join(arr)
            
            if add_op not in visited:
                visited.add(add_op)
                queue.append(add_op)
            
            # Operation 2: Rotate right by b
            rotate_op = curr[-b:] + curr[:-b]
            
            if rotate_op not in visited:
                visited.add(rotate_op)
                queue.append(rotate_op)
        
        return smallest
