import numpy as np

# Kitap fiyatları
kitap_fiyatlari = np.array([25, 45, 20, 35, 50, 40, 30])

# Satılan kitap adetleri
satis_adetleri = np.array([100, 150, 200, 120, 130, 80, 110])

# Kitap kategorileri
kategoriler = np.array(["Roman", "Bilim", "Çocuk", "Tarih", "Roman", "Bilim", "Çocuk"])

# Toplam gelir hesaplama
toplam_gelir = kitap_fiyatlari * satis_adetleri
print("Toplam Gelir:\n", kategoriler, '\n', toplam_gelir)

# Ortalama, maksimum ve minimum fiyatlar
ortalama_fiyat = np.mean(kitap_fiyatlari)
maksimum_fiyat = np.max(kitap_fiyatlari)
minimum_fiyat = np.min(kitap_fiyatlari)

print("Ortalama Fiyat: ", ortalama_fiyat, 'TL')
print("Maksimum Fiyat: ", maksimum_fiyat, 'TL')
print("Minimum Fiyat: ", minimum_fiyat, 'TL')

# Romanlar için fiyat ve satışları filtreleme
roman_fiyatlari = kitap_fiyatlari[kategoriler == "Roman"]
print('Roman Fiyatları:', roman_fiyatlari)
roman_satislari = satis_adetleri[kategoriler == "Roman"]
print('Roman Satışları:', roman_satislari)

# Romanların toplam satışları
roman_toplam_satis = np.sum(roman_fiyatlari * roman_satislari)
print('Toplam Roman Satışı:', roman_toplam_satis, 'TL')

# Daha fazla analiz için verilerin yeniden şekillendirilmesi
veri = np.array([kitap_fiyatlari, satis_adetleri])
yeniden_sekillendirilmis_veri = np.reshape(veri, (2, 7))

print(yeniden_sekillendirilmis_veri)



# 1. Kitap Fiyatları: kitap_fiyatlari dizisi, farklı kitapların fiyatlarını içerir.
# 2. Satılan Kitap Adetleri: satis_adetleri dizisi, her kitap kategorisinden satılan adetleri içerir.
# 3. Kitap Kategorileri: kategoriler dizisi, her kitap fiyatının hangi kategoriye ait olduğunu belirtir.
# 4. Toplam Gelir Hesaplama: Kitap fiyatları ile satış adetlerinin çarpımı yapılarak toplam gelir hesaplanır.
# 5. İstatistiksel Değerler: Kitap fiyatlarının ortalaması, maksimumu ve minimumu hesaplanır.
# 6. Filtreleme: Roman kategorisindeki kitapların fiyat ve satış adetleri filtrelenir.
# 7. Toplam Roman Satışı: Romanların toplam satış geliri hesaplanır.
# 8. Verilerin Yeniden Şekillendirilmesi: Kitap fiyatları ve satış adetleri, 2x7 boyutunda bir diziye dönüştürülür.