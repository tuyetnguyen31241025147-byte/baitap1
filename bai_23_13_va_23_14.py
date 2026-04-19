import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output

trucks = pd.DataFrame({
    'Xe': ['Xe 01', 'Xe 02', 'Xe 03', 'Xe 04', 'Xe 05'],
    'Tiến độ (%)': [10, 25, 5, 40, 15],
    'Trạng thái': ['Đang đi', 'Đang đi', 'Kẹt xe', 'Gần đến', 'Đang đi']
})

print("🖥️ ĐANG CẬP NHẬT DASHBOARD REAL-TIME (Mô phỏng)...")

for i in range(5):
    clear_output(wait=True)
    trucks['Tiến độ (%)'] += np.random.randint(5, 15, size=5)
    trucks.loc[trucks['Tiến độ (%)'] > 100, 'Tiến độ (%)'] = 100

    print(f"--- BÁO CÁO HỆ THỐNG GIÁM SÁT (Lần cập nhật {i+1}) ---")
    print(trucks.to_string(index=False))

    plt.barh(trucks['Xe'], trucks['Tiến độ (%)'], color='skyblue')
    plt.xlabel("Tiến độ hoàn thành (%)")
    plt.xlim(0, 100)
    plt.show()

    time.sleep(1)
