import numpy as np  # NumPy kütüphanesini içe aktarma
import pandas as pd  # Pandas kütüphanesini içe aktarma

# Excel dosyasını okuma ve bir DataFrame'e yükleme
df = pd.read_excel('C:/Users/ASUS/Desktop/Yapay_Zeka_Giris/Pandas/xlsx_dosyaları/teknolojik_urunler.xlsx')

# Kategoriye göre gruplama işlemi
gruplar = df.groupby('Kategori')

# Kategorilere göre toplam satış ve toplam fiyat işlemleri (yorum satırında)
# Kategorilere göre satış ve fiyat toplamları hesaplanabilir
# toplam_satis = df.groupby('Kategori')['Satış'].sum()
# toplam_satis_fiyat = df.groupby('Kategori')['Fiyat (TL)'].sum()

# Kategorilere göre ortalama satış fiyatını hesaplama
# ortalama_satis_fiyati = df.groupby('Kategori')['Fiyat (TL)'].mean()

# Kategorilere göre hem toplam satış hem de ortalama fiyatı aynı anda hesaplama
# 'agg' fonksiyonu birden fazla istatistiği hesaplamayı sağlar
# toplam_ve_ortalama = df.groupby('Kategori').agg(
#     {
#         'Satış':'mean',      # Ortalama satış miktarı
#         'Fiyat (TL)': 'mean' # Ortalama fiyat
#     })
# print(toplam_ve_ortalama)

# Her kategorideki en pahalı ürünü bulma
# 'idxmax' fonksiyonu, verilen sütundaki maksimum değere sahip satırın indeksini döner
# en_pahali_urun = df.loc[df.groupby('Kategori')['Fiyat (TL)'].idxmax()]
# print(en_pahali_urun)

# Satış toplamı 50'den fazla olan kategorileri filtreleme
# Bu fonksiyon, kategorilerdeki satış toplamı belirli bir değerin üstündeyse grubu döner
satis_ust_gruplar = df.groupby('Kategori').filter(lambda x: x['Satış'].sum() > 50)

# Filtrelenen kategorilerdeki ürünleri ekrana yazdırma
# Sadece kategori, ürün adı, satış ve fiyat bilgilerini gösteriyoruz
print(satis_ust_gruplar[['Kategori', 'Ürün Adı', 'Satış', 'Fiyat (TL)']])

# 1. Gruplama: df.groupby('Kategori') ile veriler kategoriye göre gruplandı.
# 2. Filtreleme: groupby ardından filter fonksiyonu ile satış toplamı 50'den fazla olan kategoriler seçildi.
# 3. İleri Analizler (Yorum Satırlarında):
#   -> Kategorilere göre toplam ve ortalama satış fiyatlarını hesaplayabilir.
#   -> Her kategorideki en pahalı ürün bulunabilir.
