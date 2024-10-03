import numpy as np
import pandas as pd

# Dosya Okuma
df = pd.read_excel('C:/Users/ASUS/Desktop/Yapay_Zeka_Giris/Pandas/xlsx_dosyaları/teknolojik_urunler1.xlsx')

# Eksik verileri True False olarak gösterme
# DataFrame'deki eksik verileri True/False olarak gösterir
# eksik_veri = df.isnull()
# print(eksik_veri)

# Null olan değerleri silme
# DataFrame'deki null (eksik) değerleri siler
# temiz_df = df.dropna()
# print(temiz_df)

# Null olan değerleri 0 ile doldurma
# DataFrame'deki null (eksik) değerleri 0 ile doldurur
doldurulmus_df = df.fillna(0)
print(doldurulmus_df)

# 'Fiyat (TL)' sütununu float veri tipine dönüştürme
# df['Fiyat (TL)'] = df['Fiyat (TL)'].astype('float')

# Yeni bir sütun ekleme
# DataFrame'e 'Yeni Sütun' adında yeni bir sütun ekler ve 1'den 20'ye kadar sayılarla doldurur
# df.insert(2, 'Yeni Sütun', range(1,21))
# print(df.head())

# DataFrame'i Excel dosyasına kaydetme
# DataFrame'i 'toexcel.xlsx' dosyasına kaydeder
# df.to_excel('toexcel.xlsx', index=False)
# print("Veri kayıt edildi!")

# 'Fiyat (TL)' sütununa göre azalan sırada sıralama
# DataFrame'i 'Fiyat (TL)' sütununa göre azalan sırada sıralar
# df_düsük = df.sort_values(by='Fiyat (TL)', ascending=False)
# print(df_düsük)

# 'Fiyat (TL)' değeri 5000'den büyük olanları filtreleme
# 'Fiyat (TL)' değeri 5000'den büyük olan satırları filtreler
# df_fiyat_ust = df[df['Fiyat (TL)']  > 5000]
# print(df_fiyat_ust)

# 'Fiyat (TL)' değeri 5000'den büyük ve 'Kategori' sütunu 'Bilgisayarlar' olanları filtreleme
# 'Fiyat (TL)' değeri 5000'den büyük ve 'Kategori' sütunu 'Bilgisayarlar' olan satırları filtreler
# df_filtreli = df[(df['Fiyat (TL)'] > 5000) & (df['Kategori'] == 'Bilgisayarlar')]
# print(df_filtreli)

# Belirli sütunları seçme
# 'Ürün Adı' ve 'Fiyat (TL)' sütunlarını seçer
# df_secili = df.loc[:,['Ürün Adı', 'Fiyat (TL)']]
# print(df_secili)

# Belirli indeks numaralarına göre satırları seçme
# İlk 12 satırı seçer
# df_ilk = df.iloc[:12,:]
# print(df_ilk)

# SQL tarzı sorgulama
# 'Satış' değeri 3'ten büyük olan satırları seçer
# df_sorgu = df.query('Satış > 3')
# print(df_sorgu)

# Belirli kategorilere göre filtreleme
# 'Kategori' sütunu 'Televizyonlar' veya 'Mobil Cihazlar' olan satırları filtreler
# df_kategoriler = df[df['Kategori'].isin(['Televizyonlar','Mobil Cihazlar'])]
# print(df_kategoriler)
