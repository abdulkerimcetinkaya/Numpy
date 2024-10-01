import numpy as np

# Bir NumPy dizisi oluşturuluyor
dizi = np.array([1, 2, 3, 4, 5])

# İstatistikleri hesaplama
minimum_deger = np.min(dizi)             # Dizideki minimum değer
maksimum_deger = np.max(dizi)             # Dizideki maksimum değer
toplam = np.sum(dizi)                     # Dizinin elemanlarının toplamı
kumulatif_toplam = np.cumsum(dizi)       # Dizinin elemanlarının kumulatif toplamı

# Sonuçları ekrana yazdırma
print("Minimum Değer:", minimum_deger)
print("Maksimum Değer:", maksimum_deger)
print("Toplam:", toplam)
print("Kumulatif Toplam:", kumulatif_toplam)


# 1. Dizi Oluşturma: dizi adında bir NumPy dizisi oluşturulur ve içinde 1'den 5'e kadar olan tam sayılar bulunmaktadır.
# 2. İstatistikleri Hesaplama:
#   -> np.min(): Dizinin içindeki en küçük değeri bulur.
#   -> np.max(): Dizinin içindeki en büyük değeri bulur.
#   -> np.sum(): Dizinin elemanlarının toplamını hesaplar.
#   -> np.cumsum(): Dizinin elemanlarının kumulatif toplamını hesaplar; yani her bir eleman için, o elemanın ve kendisinden önceki tüm elemanların toplamını döner.
# 3. Sonuçların Yazdırılması: Hesaplanan minimum değer, maksimum değer, toplam ve kumulatif toplam sonuçları ekrana yazdırılır.