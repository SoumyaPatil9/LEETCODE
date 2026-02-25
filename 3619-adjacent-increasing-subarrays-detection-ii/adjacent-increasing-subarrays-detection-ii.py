class Solution:
    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        
        segments = []
        length = 1
        
        # Step 1: build increasing segment lengths
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                length += 1
            else:
                segments.append(length)
                length = 1
        
        segments.append(length)
        
        answer = 0
        
        # Step 2: inside same segment
        for L in segments:
            answer = max(answer, L // 2)
        
        # Step 3: between adjacent segments
        for i in range(len(segments) - 1):
            answer = max(answer, min(segments[i], segments[i + 1]))
        
        return answer