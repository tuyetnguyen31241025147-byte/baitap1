import networkx as nx
import matplotlib.pyplot as plt
import random

print("🚦 Đang phân tích rủi ro kẹt xe (Bài 23.10)...")
G = nx.grid_2d_graph(5, 5)

for u, v in G.edges():
    G.edges[u, v]['weight'] = 1

ket_xe_edges = random.sample(list(G.edges()), 5)
for u, v in ket_xe_edges:
    G.edges[u, v]['weight'] = 10

start, end = (0, 0), (4, 4)

duong_ngan_nhat = nx.shortest_path(G, start, end)
duong_toi_uu = nx.shortest_path(G, start, end, weight='weight')

plt.figure(figsize=(8, 6))
pos = {(x, y): (y, -x) for x, y in G.nodes()}

nx.draw(G, pos, node_color='lightgray', node_size=200, edge_color='gray')
nx.draw_networkx_edges(G, pos, edgelist=ket_xe_edges, edge_color='red', width=4, label='Kẹt xe')
nx.draw_networkx_edges(G, pos, edgelist=[(duong_toi_uu[i], duong_toi_uu[i+1]) for i in range(len(duong_toi_uu)-1)], edge_color='green', width=4, label='Đường vòng thay thế')

plt.title("Bài 23.10: Mô hình AI tránh kẹt xe")
plt.legend(['Đường bình thường', 'Rủi ro kẹt xe', 'Tuyến đường đề xuất'])
plt.axis('off')
plt.show()
