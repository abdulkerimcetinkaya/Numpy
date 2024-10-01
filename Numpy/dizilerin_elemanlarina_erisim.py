import numpy as np

# Tek boyutlu bir NumPy dizisi oluşturuluyor
sayi_dizisi = np.array([10, 20, 30, 40, 50])

# 3. elemanı (0'dan başladığı için indeks 2) alınıyor
ucuncu_eleman = sayi_dizisi[2]
print("Üçüncü Eleman:", ucuncu_eleman)

# İki boyutlu bir NumPy matrisi oluşturuluyor
sayi_matrisi = np.array([[1, 2, 3], 
                          [4, 5, 6], 
                          [7, 8, 9]])
# Matrisi ekrana yazdırıyor
print("Matris:\n", sayi_matrisi)

# 3. satır ve 3. sütundaki elemanı (indeks [2,2]) alınıyor
matris_elemani = sayi_matrisi[2, 2]
print("3. Satır ve 3. Sütundaki Eleman:", matris_elemani)

# Dizinin son elemanı alınıyor
son_eleman = sayi_dizisi[-1]
print("Dizinin Son Elemanı:", son_eleman)

# Matrisin son satırının son elemanı alınıyor
matris_son_eleman = sayi_matrisi[-1, -1]
print("Matrisin Son Satırının Son Elemanı:", matris_son_eleman)

# Diziden ilk 3 eleman dilimleniyor
ilk_uc_eleman = sayi_dizisi[0:3]
print("İlk Üç Eleman:", ilk_uc_eleman)


# 1. Tek Boyutlu Dizi Oluşturma: sayi_dizisi adlı tek boyutlu bir NumPy dizisi oluşturuluyor.
# 2. Eleman Erişimi:
#   -> Dizinin 3. elemanı sayi_dizisi[2] ile erişiliyor ve yazdırılıyor.
# 3. İki Boyutlu Matris Oluşturma: sayi_matrisi adlı iki boyutlu bir NumPy matrisi oluşturuluyor ve yazdırılıyor.
# 4. Matris Elemanı Erişimi: Matrisin 3. satır ve 3. sütunundaki eleman sayi_matrisi[2, 2] ile alınıyor ve yazdırılıyor.
# 5. Son Eleman Erişimi:
#   -> Dizinin son elemanı sayi_dizisi[-1] ile alınıyor ve yazdırılıyor.
#   -> Matrisin son satırının son elemanı sayi_matrisi[-1, -1] ile alınıyor ve yazdırılıyor.
# 6. Dilimleme: Diziden ilk 3 eleman sayi_dizisi[0:3] ile seçiliyor ve yazdırılıyor.