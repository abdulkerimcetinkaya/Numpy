import numpy as np

# İlk NumPy dizisi oluşturuluyor
dizi1 = np.array([1, 2, 3, 5, 14])
# İkinci NumPy dizisi oluşturuluyor
dizi2 = np.array([3, 4, 12, 5])

# np.sum() dizideki elemanların toplamını verir.
# np.prod() tüm elemanları çarpar.
# np.sqrt() her bir elemanın karekökünü alır.
# np.mean() dizinin aritmetik ortalamasını verir.
# np.median() dizideki ortanca değeri bulur.
# np.std() dizinin standart sapmasını hesaplar.

# Dizinin tüm elemanlarının toplamını hesaplar
toplam = np.sum(dizi1)
# Dizinin tüm elemanlarının çarpımını hesaplar
carpma = np.prod(dizi1)
# Dizinin her bir elemanının karekökünü alır
kareal = np.sqrt(dizi1)
# Dizinin aritmetik ortalamasını hesaplar
ortalama = np.mean(dizi1)
# Dizinin medyanını (ortanca değerini) hesaplar
medyan = np.median(dizi1)
# Dizinin standart sapmasını (dağılımın ortalamadan sapmasını) hesaplar
standart_sapma = np.std(dizi1)

# Sonuçları ekrana yazdırır
print("Dizi Elemanlarının Toplamı: ", toplam)
print("Dizi Elemanlarının Çarpımı: ", carpma)
print("Dizi Elemanlarının Kare Kökü: ", kareal)
print("Dizi Elemanlarının Aritmetik Ortalaması: ", ortalama)
print("Dizi Elemanlarının Medyanı: ", medyan)
print("Dizi Elemanlarının Standart Sapması: ", standart_sapma)



# -> İlk olarak, iki adet NumPy dizisi (dizi1 ve dizi2) oluşturuluyor.
# -> Ardından, dizi1 üzerinde çeşitli istatistiksel hesaplamalar yapılıyor:
# -> Toplam: Dizi elemanlarının toplamı np.sum() ile hesaplanıyor.
# -> Çarpım: Dizi elemanlarının çarpımı np.prod() ile hesaplanıyor.
# -> Karekök: Her bir elemanın karekökü np.sqrt() ile alınıyor.
# -> Aritmetik Ortalama: Dizi elemanlarının ortalaması np.mean() ile bulunuyor.
# -> Medyan: Dizi elemanlarının medyanı np.median() ile hesaplanıyor.
# -> Standart Sapma: Dizi elemanlarının standart sapması np.std() ile hesaplanıyor.
# -> Sonuçlar, ekrana yazdırılıyor.