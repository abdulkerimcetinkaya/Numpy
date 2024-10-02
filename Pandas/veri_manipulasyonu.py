import numpy as np
import pandas as pd

# Dosya Okuma
df = pd.read_excel('C:/Users/ASUS/Desktop/Yapay_Zeka_Giris/Pandas/xlsx_dosyaları/teknolojik_urunler1.xlsx')

# Eksik verileri True False olarak gösterme
# eksik_veri = df.isnull()
# print(eksik_veri)

# Null olan değerleri silme
# temiz_df = df.dropna()
# print(temiz_df)

doldurulmus_df = df.fillna(0)
print(doldurulmus_df)
# df['Fiyat (TL)'] = df['Fiyat (TL)'].astype('float')
# df.insert(2, 'Yeni Sütun', range(1,21))
# print(df.head())
# df.to_excel('toexcel.xlsx', index=False)
# print("Veri kayıt edildi!")
# df_düsük = df.sort_values(by='Fiyat (TL)', ascending=False)
# print(df_düsük)
# df_fiyat_ust = df[df['Fiyat (TL)']  > 5000]
# print(df_fiyat_ust)

# df_filtreli = df[(df['Fiyat (TL)'] > 5000) & (df['Kategori'] == 'Bilgisayarlar')]
# print(df_filtreli)
# df_secili = df.loc[:,['Ürün Adı', 'Fiyat (TL)']]
# print(df_secili)
#index numarasına göre seçer
# df_ilk = df.iloc[:12,:]
# print(df_ilk)
#SQL tarzı sorgulama

# df_sorgu = df.query('Satış > 3')
# print(df_sorgu)

# df_kategoriler = df[df['Kategori'].isin(['Televizyonlar','Mobil Cihazlar'])]
# print(df_kategoriler)