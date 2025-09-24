def draw_ascii(path, graph=None):
    # Calculate total distance if graph is provided
    total_distance = 0
    if graph:
        for i in range(len(path)-1):
            city1 = path[i]
            city2 = path[i+1]
            if city2 in graph.get(city1, {}):
                total_distance += graph[city1][city2]
            elif city1 in graph.get(city2, {}):
                total_distance += graph[city2][city1]

    # Print path with arrows
    print(" -> ".join(path))
    if graph:
        print(f"Total Jarak: {total_distance} km")
