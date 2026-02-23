class Solution:
    def countValidSelections(self, nums):
        n = len(nums)
        answer = 0
        
        for start in range(n):
            if nums[start] != 0:
                continue
            
            for direction in (-1, 1):
                arr = nums[:]   # copy
                curr = start
                d = direction
                
                while 0 <= curr < n:
                    if arr[curr] == 0:
                        curr += d
                    else:
                        arr[curr] -= 1
                        d *= -1
                        curr += d
                
                if all(x == 0 for x in arr):
                    answer += 1
        
        return answer