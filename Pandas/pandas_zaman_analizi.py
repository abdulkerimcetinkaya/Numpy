import pandas as pd  # pandas kütüphanesini içe aktarma
import matplotlib.pyplot as plt  # matplotlib kütüphanesini içe aktarma

# Excel dosyasının yolu
df = pd.read_excel('C:/Users/ASUS/Desktop/Yapay_Zeka_Giris/Pandas/xlsx_dosyaları/teknolojik_urunler.xlsx')

# Tarih sütununu datetime formatına çevirme
df['Tarih'] = pd.to_datetime(df['Tarih'])

# Tarih sütununu indeks olarak ayarlama ve sıralama
df.set_index('Tarih', inplace=True)
df = df.sort_index()

# 1. En yüksek satışın yapıldığı ay ve o ayda satılan ürünler
aylik_satis = df.resample('ME')['Satış'].sum()  # Aylık toplam satışları hesaplama
max_ay = aylik_satis.idxmax()  # En yüksek satış yapılan ayı bulma
max_satis_ay = aylik_satis.max()  # En yüksek satış miktarını bulma
max_satis_ay_urunler = df[df.index.to_series().between(max_ay - pd.offsets.MonthBegin(1), max_ay)]  # O ayda satılan ürünleri bulma

# En yüksek satış yapılan ay ve o ayda satılan ürünleri yazdırma
print(f"En yüksek satış yapılan ay: {max_ay} - Toplam satış: {max_satis_ay}")
print("O ayda satılan ürünler:")
print(max_satis_ay_urunler[['Ürün Adı', 'Satış']])

# 2. En düşük satışın yapıldığı ay ve o ayda satılan ürünler
min_ay = aylik_satis.idxmin()  # En düşük satış yapılan ayı bulma
min_satis_ay = aylik_satis.min()  # En düşük satış miktarını bulma
min_satis_ay_urunler = df[df.index.to_series().between(min_ay - pd.offsets.MonthBegin(1), min_ay)]  # O ayda satılan ürünleri bulma

# En düşük satış yapılan ay ve o ayda satılan ürünleri yazdırma
print(f"En düşük satış yapılan ay: {min_ay} - Toplam satış: {min_satis_ay}")
print("O ayda satılan ürünler:")
print(min_satis_ay_urunler[['Ürün Adı', 'Satış']])

# 3. En fazla satış yapılan gün ve o gün satılan ürünler
gunluk_satis = df.resample('D')['Satış'].sum()  # Günlük toplam satışları hesaplama
max_gun = gunluk_satis.idxmax()  # En fazla satış yapılan günü bulma
max_satis_gun = gunluk_satis.max()  # En fazla satış miktarını bulma
max_satis_gun_urunler = df.loc[max_gun]  # O gün satılan ürünleri bulma

# En fazla satış yapılan gün ve o gün satılan ürünleri yazdırma
print(f"\nEn fazla satış yapılan gün: {max_gun} - Toplam satış: {max_satis_gun}")
print('O günde satılan ürünler:')
print(max_satis_gun_urunler[['Ürün Adı', 'Satış']])

# 4. Haftalık en fazla satış yapılan ürünler
haftalik_satis = df.resample('W')['Satış'].sum()  # Haftalık toplam satışları hesaplama
max_hafta = haftalik_satis.idxmax()  # En fazla satış yapılan haftayı bulma
max_satis_hafta = haftalik_satis.max()  # En fazla satış miktarını bulma
max_satis_hafta_urunler = df[df.index.to_series().between(max_hafta - pd.offsets.Week(1), max_hafta)]  # O hafta satılan ürünleri bulma

# En fazla satış yapılan hafta ve o hafta satılan ürünleri yazdırma
print(f"\nEn fazla satış yapılan hafta: {max_hafta} - Toplam satış: {max_satis_hafta}")
print("O hafta satılan ürünler:")
print(max_satis_hafta_urunler[['Ürün Adı', 'Satış']])

# Aylık ortalama satışlar
aylik_ortalama_satis = df.resample('ME')['Satış'].mean()  # Aylık ortalama satışları hesaplama
print('Aylık ortalama satışlar:')
print(aylik_ortalama_satis)

# Belirli aralıkta satılan ürünler
belirli_aralik_urunler = df[df.index.to_series().between('2024-01-01', '2024-03-31')]  # Belirli tarih aralığında satılan ürünleri bulma
print("Ocak 2024 ile Mart 2024 arasında satılan ürünler:")
print(belirli_aralik_urunler[['Ürün Adı', 'Satış', 'Fiyat (TL)', 'Toplam Fiyat (TL)']])

# 8. En yüksek toplam fiyatın olduğu ay ve o ayda satılan ürünler
aylik_toplam_fiyat = df.resample('ME')['Toplam Fiyat (TL)'].sum()  # Aylık toplam fiyatları hesaplama
max_ay_fiyat = aylik_toplam_fiyat.idxmax()  # En yüksek toplam fiyata sahip ayı bulma
max_fiyat_ay = aylik_toplam_fiyat.max()  # En yüksek toplam fiyatı bulma
max_fiyat_ay_urunler = df[df.index.to_series().between(max_ay_fiyat - pd.offsets.MonthBegin(1), max_ay_fiyat)]  # O ayda satılan ürünleri bulma

# En yüksek toplam fiyata sahip ay ve o ayda satılan ürünleri yazdırma
print(f"En yüksek toplam fiyata sahip ay: {max_ay_fiyat} - Toplam fiyat: {max_fiyat_ay}")
print("O ayda satılan ürünler:")
print(max_fiyat_ay_urunler[['Satış', 'Ürün Adı', 'Toplam Fiyat (TL)']])

# Satışların zaman içindeki değişimi grafiği
df['Satış'].plot(title='Satışların Zaman İçindeki Değişimi', xlabel='Tarih', ylabel='Satış Miktarı')
plt.show()  # Grafiği gösterme
