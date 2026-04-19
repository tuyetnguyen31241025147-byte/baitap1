import folium
import numpy as np
from folium.plugins import HeatMap

center = (10.7613, 106.6687)
m2 = folium.Map(location=center, zoom_start=13)

heat_data = [[10.761 + np.random.normal(0, 0.02), 106.668 + np.random.normal(0, 0.02)] for _ in range(300)]
HeatMap(heat_data, radius=12).add_to(m2)

folium.Circle(center, radius=3000, color='green', weight=2, fill=False, tooltip="Vùng 3km").add_to(m2)
folium.Circle(center, radius=5000, color='orange', weight=2, fill=False, tooltip="Vùng 5km").add_to(m2)
folium.Circle(center, radius=10000, color='red', weight=2, fill=False, tooltip="Vùng 10km").add_to(m2)

m2
