import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import folium

print("📈 Đang chạy mô hình ML dự đoán nhu cầu (Bài 23.11)...")

data = []
for _ in range(500):
    lat = 10.76 + np.random.uniform(-0.02, 0.02)
    lon = 106.66 + np.random.uniform(-0.02, 0.02)
    hour = np.random.randint(6, 22)
    rain = np.random.randint(0, 2)
    demand = int((hour == 17) * 50 + rain * 80 + np.random.randint(10, 30))
    data.append([lat, lon, hour, rain, demand])

df = pd.DataFrame(data, columns=['Lat', 'Lon', 'Hour', 'Rain', 'Demand'])

X = df[['Lat', 'Lon', 'Hour', 'Rain']]
y = df['Demand']
model = RandomForestRegressor(n_estimators=50, random_state=42)
model.fit(X, y)

m_predict = folium.Map(location=[10.76, 106.66], zoom_start=14)
test_points = df.sample(20)[['Lat', 'Lon']]
test_points['Hour'] = 17
test_points['Rain'] = 1
test_points['Predicted_Demand'] = model.predict(test_points[['Lat', 'Lon', 'Hour', 'Rain']])

for _, row in test_points.iterrows():
    color = 'red' if row['Predicted_Demand'] > 100 else 'orange' if row['Predicted_Demand'] > 50 else 'green'
    folium.CircleMarker(
        location=[row['Lat'], row['Lon']],
        radius=row['Predicted_Demand'] / 10,
        color=color, fill=True,
        popup=f"Dự báo nhu cầu: {int(row['Predicted_Demand'])} yêu cầu"
    ).add_to(m_predict)

print("-> Khu vực chấm đỏ cần điều tiết thêm nhân sự/xe cộ ngay lập tức.")
