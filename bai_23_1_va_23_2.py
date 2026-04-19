import folium
from geopy.distance import geodesic

center = (10.7613, 106.6687)
m = folium.Map(location=center, zoom_start=14)

locations = [
    {"name": "Bệnh viện Chợ Rẫy", "coords": (10.7573, 106.6575)},
    {"name": "Vạn Hạnh Mall", "coords": (10.7706, 106.6713)},
    {"name": "UBND Quận 10", "coords": (10.7712, 106.6661)},
    {"name": "Bến xe Lê Hồng Phong", "coords": (10.7635, 106.6738)},
    {"name": "Ký túc xá UEH", "coords": (10.7600, 106.6650)}
]

layer_center = folium.FeatureGroup(name="Trung tâm").add_to(m)
layer_pois = folium.FeatureGroup(name="Các điểm lân cận").add_to(m)

folium.Marker(center, popup="Điểm trung tâm", icon=folium.Icon(color='red')).add_to(layer_center)

for loc in locations:
    dist = geodesic(center, loc["coords"]).kilometers
    folium.Marker(
        loc["coords"],
        popup=f"{loc['name']}<br>Cách tâm: {dist:.2f}km"
    ).add_to(layer_pois)

folium.LayerControl().add_to(m)
m
