import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Veriyi hazırlama
data = {
    'Ev_Buyuklugu': [120, 250, 175, 300, 220],  # Ev büyüklükleri (m²)
    'Oda_Sayisi': [3, 5, 4, 6, 4],  # Oda sayıları
    'Fiyat': [2400000, 5000000, 3500000, 6000000, 4400000]  # Ev fiyatları (TL)
}

# Veriyi DataFrame'e çevirme
df = pd.DataFrame(data)

# Girdi ve çıktı değişkenlerini belirleme
X = df[['Ev_Buyuklugu', 'Oda_Sayisi']]  # Girdi: Ev büyüklüğü ve oda sayısı
y = df['Fiyat']  # Çıktı: Fiyat

# Veriyi eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluşturma ve eğitme
model = LinearRegression()
model.fit(X_train, y_train)

# Kullanıcıdan ev büyüklüğünü ve oda sayısını alma
ev_buyuklugu = float(input("Lütfen evin büyüklüğünü (m²) girin: "))
oda_sayisi = int(input("Lütfen oda sayısını girin: "))

# Tahmini fiyatı hesaplama
tahmini_fiyat = model.predict([[ev_buyuklugu, oda_sayisi]])

# Tahmini fiyatı ekrana yazdırma
print(f'Bu evin tahmini fiyatı: {tahmini_fiyat[0]:.3f} TL')
