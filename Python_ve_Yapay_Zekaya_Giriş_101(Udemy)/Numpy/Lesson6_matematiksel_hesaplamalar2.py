import numpy as np

# İki adet NumPy dizisi oluşturuluyor
dizi1 = np.array([1, 2, 3, 4, 5])
dizi2 = np.array([3, 4, 38, 44, 51])

# Matematiksel işlemler:
toplam = np.add(dizi1, dizi2)           # Eleman bazında toplama
fark = np.subtract(dizi1, dizi2)        # Eleman bazında çıkarma
carpim = np.multiply(dizi1, dizi2)      # Eleman bazında çarpma
bölüm = np.divide(dizi1, dizi2)         # Eleman bazında bölme
kare = np.power(dizi1, 2)                # dizi1'in elemanlarının karesi
karekök = np.sqrt(dizi1)                # dizi1'in elemanlarının karekökü
ortalama = np.mean(dizi1)               # dizi1'in aritmetik ortalaması
varyans = np.var(dizi1)                 # dizi1'in varyansı
standart_sapma = np.std(dizi1)          # dizi1'in standart sapması

# Sonuçlar ekrana yazdırılıyor
print("Toplam: ", toplam)
print("Fark: ", fark)
print("Çarpım: ", carpim)
print("Bölüm: ", bölüm)
print("Karesi: ", kare)
print("Karekök: ", karekök)
print("Ortalama: ", ortalama)
print("Varyans: ", varyans)
print("Standart Sapma: ", standart_sapma)


# 1. Dizi Oluşturma: dizi1 ve dizi2 adında iki adet NumPy dizisi oluşturuluyor.
# 2. Matematiksel İşlemler:
#   -> np.add(): İki dizinin elemanlarını toplar.
#   -> np.subtract(): İki dizinin elemanlarını çıkarır.
#   -> np.multiply(): İki dizinin elemanlarını çarpar.
#   -> np.divide(): İki dizinin elemanlarını böler.
#   -> np.power(): dizi1'in elemanlarının karesini alır.
#   -> np.sqrt(): dizi1'in elemanlarının karekökünü alır.
#   -> np.mean(): dizi1'in aritmetik ortalamasını hesaplar.
#   -> np.var(): dizi1'in varyansını hesaplar.
#   -> np.std(): dizi1'in standart sapmasını hesaplar.
# 3. Sonuçların Yazdırılması: Her bir işlem sonucunu ekrana yazdırır.