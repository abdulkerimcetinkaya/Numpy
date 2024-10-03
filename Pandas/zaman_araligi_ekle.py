import pandas as pd
import numpy as np

# Excel dosyasını oku
df = pd.read_excel('C:/Users/ASUS/Desktop/Yapay_Zeka_Giris/Pandas/xlsx_dosyaları/teknolojik_urunler.xlsx')

# Rastgele tarih damgaları oluşturma
df['Tarih'] = pd.to_datetime(np.random.choice(pd.date_range('2024-01-01','2024-12-31'), size=len(df)))

print(df.head())

df.to_excel('teknolojik_urunler_zamanli.xlsx')
print("Veri dosyaya aktarıldı.")