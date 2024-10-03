import pandas as pd
import numpy as np

# Excel dosyasını oku
# Belirtilen dosya yolundaki Excel dosyasını okur ve bir DataFrame oluşturur
df = pd.read_excel('C:/Users/ASUS/Desktop/Yapay_Zeka_Giris/Pandas/xlsx_dosyaları/teknolojik_urunler.xlsx')

# Rastgele tarih damgaları oluşturma
# 2024 yılı içindeki rastgele tarihleri seçer ve 'Tarih' sütununa ekler
df['Tarih'] = pd.to_datetime(np.random.choice(pd.date_range('2024-01-01','2024-12-31'), size=len(df)))

# İlk birkaç satırı yazdırma
# DataFrame'in ilk 5 satırını yazdırır
print(df.head())

# DataFrame'i yeni bir Excel dosyasına kaydetme
# Güncellenmiş DataFrame'i 'teknolojik_urunler_zamanli.xlsx' dosyasına kaydeder
df.to_excel('teknolojik_urunler_zamanli.xlsx')
print("Veri dosyaya aktarıldı.")
