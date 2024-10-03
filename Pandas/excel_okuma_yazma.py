import numpy as np  # NumPy kütüphanesini içe aktarma
import pandas as pd  # Pandas kütüphanesini içe aktarma

# Excel dosyasını okuma ve bir DataFrame'e yükleme
df = pd.read_excel('C:/Users/ASUS/Desktop/Yapay_Zeka_Giris/Pandas/xlsx_dosyaları/teknolojik_urunler.xlsx')

# İlk 3 satırı getirmek için kullanılan kod (şu an yorum satırına alınmış)
# Bu, veri yapısının genel görünümü hakkında fikir verir
# print(df.head())

# Tüm ürünlerin ortalama fiyatını hesaplama
ortalama_fiyat = df['Fiyat (TL)'].mean()

# Hesaplanan ortalama fiyatı ekrana yazdırma (şu an yorum satırında)
# print(f"Ortalama Fiyat : {ortalama_fiyat} TL")

# Kategorilere göre toplam satış miktarını hesaplama
kategori_bazlı_satıs = df.groupby('Kategori')['Satış'].sum()

# Kategori bazlı satışları ekrana yazdırma (şu an yorum satırında)
# print(f"{kategori_bazlı_satıs}")

# En çok gelir getiren ürünü bulma
# 'Toplam Fiyat (TL)' sütununda en yüksek değere sahip olan ürünü bulur
# max_gelir = df.loc[df['Toplam Fiyat (TL)'].idxmax()]
# print(f"En çok gelir getiren ürün : {max_gelir}")

# Fiyatı 4000 TL'den yüksek olan ürünleri filtreleme
fiyat_ustunu_getir = df[df['Fiyat (TL)'] > 4000]
print(f"4000 TL'den yüksek ürünler : {fiyat_ustunu_getir}")

# Filtrelenen ürünleri yeni bir Excel dosyasına kaydetme
fiyat_ustunu_getir.to_excel('Fiyatı 4000 TL üstü olanlar.xlsx')

# 1. Bir Excel dosyasını pandas kütüphanesiyle okur.
# 2. Verilerin ilk 3 satırını gösterebilir (şu an yorum satırında).
# 3. Ürünlerin ortalama fiyatını hesaplar.
# 4. Kategorilere göre satışları gruplar ve toplar.
# 5. Fiyatı 4000 TL'den yüksek olan ürünleri filtreler ve sonucu yeni bir Excel dosyasına yazar.
