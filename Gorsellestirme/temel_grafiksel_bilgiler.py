import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dosya Okuma
df = pd.read_excel('C:/Users/ASUS/Desktop/Yapay_Zeka_Giris/Pandas/xlsx_dosyaları/teknolojik_urunler_zamanli.xlsx')
df['Tarih'] = pd.to_datetime(df['Tarih'])
df.set_index('Tarih', inplace=True)

# Satışların zaman içinde ki değişimini gösteren bir çizgi grafiği
df['Satış'].plot(title='Satışların Zaman İçindeki Değişimi', xlabel='Tarih', ylabel='Satış Miktarı')
aylik_satis = df.resample('ME')['Satış'].sum()
aylik_satis.plot(kind='bar', title='Aylık toplam Satışlar', xlabel='Ay', ylabel='Toplam Satışı')
plt.show()