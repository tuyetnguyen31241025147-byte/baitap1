import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

coords = np.random.rand(50, 2) * 10

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10).fit(coords)
kho_hang = kmeans.cluster_centers_

df_donhang = pd.DataFrame(coords, columns=['Vĩ độ', 'Kinh độ'])
df_donhang['Mã Trạm Gán'] = kmeans.labels_

print("Bảng gán xe mô phỏng (Bài 23.8):")
print(df_donhang.head(10))

plt.figure(figsize=(7, 5))
plt.scatter(coords[:, 0], coords[:, 1], c=kmeans.labels_, cmap='tab10', alpha=0.7, label='Điểm giao')
plt.scatter(kho_hang[:, 0], kho_hang[:, 1], c='red', marker='s', s=150, label='Trạm/Kho (AI đề xuất)')
plt.title("Bài 23.8 & 23.9: Phân cụm và Gán trạm bằng K-Means")
plt.legend()
plt.show()
