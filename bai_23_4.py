import geopandas as gpd
import osmnx as ox
import matplotlib.pyplot as plt
import random

print("Đang tải dữ liệu ranh giới bằng GeoPandas/OSMnx...")
districts = ox.geocode_to_gdf(["Quận 1, Ho Chi Minh City", "Quận 3, Ho Chi Minh City", "Quận 10, Ho Chi Minh City", "Quận 5, Ho Chi Minh City"])

districts['don_hang'] = [random.randint(1000, 5000) for _ in range(len(districts))]

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
districts.plot(column='don_hang', cmap='OrRd', legend=True,
               edgecolor='black', ax=ax,
               legend_kwds={'label': "Số lượng đơn hàng"})

plt.title("Bài 23.4: Bản đồ Choropleth theo ranh giới Quận")
plt.axis('off')
plt.show()
