/ author mansoor.wani.king
import heapq
import math

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        self.dist = math.inf
        self.prev = None

def dijkstra_search(graph, start, goal):
    start.dist = 0
    pq = [(0, start)]
    while pq:
        dist_u, u = heapq.heappop(pq)
        if u == goal:
            break
        if dist_u > u.dist:
            continue
        for v, weight in u.neighbors:
            alt = dist_u + weight
            if alt < v.dist:
                v.dist = alt
                v.prev = u
                heapq.heappush(pq, (alt, v))
    path = []
    curr = goal
    while curr:
        path.append(curr)
        curr = curr.prev
    path.reverse()
    return path

def main():
    # Example input data
    obstacles = [[(1, 1), (3, 1), (3, 3), (1, 3)], [(5, 5), (7, 5), (7, 7), (5, 7)]]
    bounds = [(0, 0), (10, 10)]
    start_node = Node(1, 1)
    goal_node = Node(9, 9)

    # Step 1: Generate Voronoi diagram
    voronoi_graph = generate_voronoi_diagram(obstacles, bounds)

    # Step 2: Calculate energy consumption model
    current_state = {}  # Assuming current state is given
    energy_consumption = calculate_energy_consumption(voronoi_graph, current_state)

    # Step 3: Dijkstra search
    initial_path = dijkstra_search(voronoi_graph, start_node, goal_node)

    # Step 4: Visibility algorithm for path optimization
    optimized_path = visibility_algorithm(voronoi_graph, start_node, goal_node)

    # Step 5: Optimize path
    final_path = optimize_path(optimized_path)

    print("Final Path:", final_path)

if __name__ == "__main__":
    main()

