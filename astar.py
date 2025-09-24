import heapq

def heuristic(city):
    coords = {
        "Cilegon": (0, 0),
        "Tangerang": (4, 0),
        "Jakarta": (8, 0),
        "Depok": (8, 2),
        "Bogor": (8, 4),
        "Sukabumi": (8, 6),
        "Bandung": (12, 6),
        "Bekasi": (12, 0),
        "Indramayu": (16, 0),
        "Subang": (16, 2),
        "Cirebon": (20, 0),
        "Tegal": (24, 0),
        "Pekalongan": (28, 0),
        "Semarang": (32, 0),
        "Kudus": (36, 0),
        "Rembang": (40, 0),
        "Tuban": (44, 0),
        "Bojonegoro": (48, 0),
        "Ngawi": (52, 0),
        "Surakarta": (56, 0),
        "Surabaya": (60, 0),
        "Sidoarjo": (64, 0),
        "Probolinggo": (68, 0),
        "Situbondo": (72, 0),
        "Banyuwangi": (76, 0),
        "Jember": (76, 2),
        "Lumajang": (72, 2),
        "Nganjuk": (64, 2),
        "Kepanjen": (68, 2),
        "Trenggalek": (60, 2),
        "Pacitan": (56, 2),
        "Purwokerto": (20, 4),
        "Cilacap": (20, 6),
        "Kebumen": (24, 4),
        "Yogyakarta": (28, 4),
        "Magelang": (28, 2),
        "Ambarawa": (28, 0),
        "Tasikmalaya": (16, 6),
    }
    bx, by = coords["Banyuwangi"]
    x, y = coords[city]
    return abs(bx - x) + abs(by - y)

def astar(graph, start, goal):
    queue = [(heuristic(start), 0, start, [start])]
    visited = set()
    while queue:
        est_total, cost, node, path = heapq.heappop(queue)
        if node == goal:
            return path, cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                new_cost = cost + weight
                est = new_cost + heuristic(neighbor)
                heapq.heappush(queue, (est, new_cost, neighbor, path + [neighbor]))
    return None, float('inf')
