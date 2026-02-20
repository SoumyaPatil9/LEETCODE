class Solution:
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)
        
        capacity.sort(reverse=True)
        
        total_capacity = 0
        boxes_used = 0
        
        for cap in capacity:
            total_capacity += cap
            boxes_used += 1
            if total_capacity >= total_apples:
                return boxes_used
