def ids(graph, start, goal, max_depth=50):
    def dls(node, goal, depth, path, cost):
        if node == goal:
            return path, cost
        if depth == 0:
            return None, float('inf')
        for neighbor, weight in graph[node].items():
            if neighbor not in path:
                result, total_cost = dls(neighbor, goal, depth-1, path+[neighbor], cost+weight)
                if result:
                    return result, total_cost
        return None, float('inf')
    for depth in range(max_depth):
        result, total_cost = dls(start, goal, depth, [start], 0)
        if result:
            return result, total_cost
    return None, float('inf')
