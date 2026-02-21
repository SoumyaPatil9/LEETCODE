class Solution:
    def countCollisions(self, directions):
        n = len(directions)
        
        left = 0
        while left < n and directions[left] == 'L':
            left += 1
        
        right = n - 1
        while right >= 0 and directions[right] == 'R':
            right -= 1
        
        collisions = 0
        
        for i in range(left, right + 1):
            if directions[i] != 'S':
                collisions += 1
        
        return collisions