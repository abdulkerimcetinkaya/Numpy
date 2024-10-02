import numpy as np
import pandas as pd

# Dosya Okuma
df = pd.read_excel('C:/Users/ASUS/Desktop/Yapay_Zeka_Giris/Pandas/xlsx_dosyaları/teknolojik_urunler.xlsx')

# İlk 3 satırı getir
# print(df.head())

ortalama_fiyat = df['Fiyat (TL)'].mean()
# print(f"Ortalam Fiyat : {ortalama_fiyat} TL" )

# en çok gelir getiren ürünü sıralama
kategori_bazlı_satıs = df.groupby('Kategori')['Satış'].sum()
# print(f"{kategori_bazlı_satıs}")

#En çok gelir getiren ürünü bulma
# max_gelir = df.loc[df['Toplam Fiyat (TL)'].idxmax()]
# print(f"En çok gelir getiren ürün : {max_gelir}")

# Belirli bir fiyat üstünü getir
fiyat_ustunu_getir = df[df['Fiyat (TL)'] > 4000]
print(f"4000 TL den yüksek ürünler : {fiyat_ustunu_getir}")

fiyat_ustunu_getir.to_excel('Fiyatı 4000 TL üstü olanlar.xlsx')