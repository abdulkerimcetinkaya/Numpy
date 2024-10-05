import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Veriyi hazırlama
data = {
    'Ev_Buyuklugu': [120, 250, 175, 300, 220],  # Ev büyüklükleri (m²)
    'Fiyat': [2400000, 5000000, 3500000, 6000000, 4400000]  # Ev fiyatları (TL)
}

# Veriyi DataFrame'e çevirme
df = pd.DataFrame(data)

# Girdi ve çıktı değişkenlerini belirleme
X = df[['Ev_Buyuklugu']]  # Girdi: Ev büyüklüğü
y = df['Fiyat']  # Çıktı: Fiyat

# Veriyi eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluşturma ve eğitme
model = LinearRegression()
model.fit(X_train, y_train)

# Kullanıcıdan ev büyüklüğünü alma
ev_buyuklugu = float(input("Lütfen evin büyüklüğünü (m²) girin: "))

# Tahmini fiyatı hesaplama
tahmini_fiyat = model.predict([[ev_buyuklugu]])

# Tahmini fiyatı ekrana yazdırma
print(f"Bu evin tahmini fiyatı: {tahmini_fiyat[0]:.2f} TL")
