import numpy as np

# İki adet NumPy dizisi oluşturuluyor
dizi1 = np.array([1, 2, 3, 4, 5])
dizi2 = np.array([3, 4, 38, 44, 51])

# Matematiksel işlemler:
toplam = np.add(dizi1, dizi2)           # Eleman bazında toplama
fark = np.subtract(dizi1, dizi2)        # Eleman bazında çıkarma
carpim = np.multiply(dizi1, dizi2)      # Eleman bazında çarpma
böl = np.divide(dizi1, dizi2)           # Eleman bazında bölme
ust = np.power(dizi1, 2)                # Elemanların karesi (dizi1^2)
karekok = np.sqrt(dizi1)                # Elemanların karekökü
ortalama = np.mean(dizi1)               # dizi1'in aritmetik ortalaması
varyans = np.var(dizi1)                 # dizi1'in varyansı
standart_sapma = np.std(dizi1)          # dizi1'in standart sapması

# Sonuçlar ekrana yazdırılıyor
print("Toplam: ", toplam)
print("Fark: ", fark)
print("Çarpım: ", carpim)
print("Bölüm: ", böl)
print("Karesi: ", ust)
print("Karekök: ", karekok)
print("Ortalama: ", ortalama)
print("Varyans: ", varyans)
print("Standart Sapma: ", standart_sapma)
