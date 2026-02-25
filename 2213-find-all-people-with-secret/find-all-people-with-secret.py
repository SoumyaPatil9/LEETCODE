class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        # Person 0 and firstPerson know secret initially
        union(0, firstPerson)
        
        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])
        
        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            temp = []
            
            # Process same-time meetings
            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                union(x, y)
                temp.append(x)
                temp.append(y)
                i += 1
            
            # After union, check who is connected to 0
            for person in set(temp):
                if find(person) != find(0):
                    parent[person] = person  # reset
        
        # Collect all connected to 0
        root0 = find(0)
        return [i for i in range(n) if find(i) == root0]