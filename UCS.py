def ucs(start, goal):
    frontier = [(0, [start])]
    visited = set()
    while frontier:
        cost, path = heapq.heappop(frontier)
        node = path[-1]
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, c in graph.get(node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(frontier, (cost + c, path + [neighbor]))
    return None, float("inf")
