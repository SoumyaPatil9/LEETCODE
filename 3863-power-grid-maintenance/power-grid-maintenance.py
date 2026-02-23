import heapq

class Solution:
    def processQueries(self, c, connections, queries):
        # ---------- DSU ----------
        parent = list(range(c + 1))
        rank = [0] * (c + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if rank[px] < rank[py]:
                    parent[px] = py
                elif rank[px] > rank[py]:
                    parent[py] = px
                else:
                    parent[py] = px
                    rank[px] += 1

        # Build connected components
        for u, v in connections:
            union(u, v)

        # ---------- Build heaps for each component ----------
        comp = {}
        for i in range(1, c + 1):
            root = find(i)
            if root not in comp:
                comp[root] = []
            heapq.heappush(comp[root], i)

        # Track online status
        online = [True] * (c + 1)

        result = []

        # ---------- Process queries ----------
        for t, x in queries:
            if t == 1:
                if online[x]:
                    result.append(x)
                else:
                    root = find(x)
                    heap = comp[root]

                    # Lazy deletion of offline stations
                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)

                    if heap:
                        result.append(heap[0])
                    else:
                        result.append(-1)

            else:  # t == 2
                online[x] = False

        return result