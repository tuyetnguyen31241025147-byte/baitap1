import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance_matrix

print("🚚 Đang chạy thuật toán Tối ưu hóa điều phối (Bài 23.12)...")
locations = np.random.rand(11, 2) * 10
kho = locations[0]
khach_hang = locations[1:]

plt.figure(figsize=(8, 6))
plt.scatter(khach_hang[:, 0], khach_hang[:, 1], c='blue', label='Khách hàng')
plt.scatter(kho[0], kho[1], c='black', marker='s', s=200, label='Kho trung tâm')

xe_1 = [i for i in range(1, 11) if locations[i][0] < 5]
xe_2 = [i for i in range(1, 11) if locations[i][0] >= 5]

def draw_route(vehicle_nodes, color, label):
    if not vehicle_nodes: return
    current = 0
    unvisited = vehicle_nodes.copy()
    route_x, route_y = [locations[current][0]], [locations[current][1]]

    while unvisited:
        next_node = min(unvisited, key=lambda x: np.linalg.norm(locations[current] - locations[x]))
        route_x.append(locations[next_node][0])
        route_y.append(locations[next_node][1])
        unvisited.remove(next_node)
        current = next_node

    route_x.append(locations[0][0])
    route_y.append(locations[0][1])
    plt.plot(route_x, route_y, c=color, linewidth=2, marker='o', label=label)

draw_route(xe_1, 'orange', 'Lộ trình Xe 1')
draw_route(xe_2, 'purple', 'Lộ trình Xe 2')

plt.title("Bài 23.12: Giải bài toán VRP (Heuristic)")
plt.legend()
plt.show()
