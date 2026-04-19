import osmnx as ox
import networkx as nx

center = (10.7613, 106.6687)
print("Đang tải dữ liệu đường phố thật (Bán kính 800m)...")
G = ox.graph_from_point(center, dist=800, network_type="drive")

nodes = list(G.nodes())
start_node = nodes[10]
end_node = nodes[-10]

shortest_path = nx.shortest_path(G, source=start_node, target=end_node, weight='length')

fig, ax = ox.plot_graph_route(G, shortest_path, route_color='red', route_linewidth=4, node_size=2)
