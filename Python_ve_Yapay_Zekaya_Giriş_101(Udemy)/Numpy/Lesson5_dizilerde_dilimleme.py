import numpy as np

# Tek boyutlu bir NumPy dizisi oluşturuluyor
dizi = np.array([10, 20, 30, 40, 50])

# 3. elemanı (0'dan başladığı için indeks 2) seçiliyor
ucuncu_eleman = dizi[2]
# print(ucuncu_eleman)  # Seçilen elemanı yazdırmak için yorum satırını kaldırın

# İki boyutlu bir NumPy matrisi oluşturuluyor
matris = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
# print(matris)  # Matrisi yazdırmak için yorum satırını kaldırın

# 3. satır ve 3. sütundaki elemanı (indeks [2,2]) alınıyor
matris_elemani = matris[2, 2]
# print(matris_elemani)  # Seçilen elemanı yazdırmak için yorum satırını kaldırın

# Dizinin son elemanına negatif indeksleme ile erişiliyor
print("Dizinin Son Elemanı:", dizi[-1])

# Matrisin son satırının son elemanına negatif indeksleme ile erişiliyor
print("Matrisin Son Satırının Son Elemanı:", matris[-1, -1])

# Diziden ilk 3 elemanı (0'dan 2. indekse kadar) dilimleme ile seçiliyor
dilimli_dizi = dizi[0:3]
print("Dilimli Dizi:", dilimli_dizi)

# 0 ve 1. satır ile 1 ve 2. sütunları seçerek bir alt matris oluşturuluyor
alt_matris = matris[0:2, 1:3]
print("Alt Matris:\n", alt_matris)


# 1. Tek Boyutlu Dizi Oluşturma: dizi adında bir NumPy dizisi oluşturuluyor.
# 2. Eleman Erişimi:
#   -> Dizinin 3. elemanı (indeks 2) alınıyor.
# 3. İki Boyutlu Matris Oluşturma: matris adında bir iki boyutlu NumPy matrisi oluşturuluyor.
# 4. Matris Elemanı Erişimi: Matrisin 3. satır ve 3. sütunundaki eleman alınıyor.
# 5. Son Eleman Erişimi:
#   -> Dizinin son elemanına dizi[-1] ile erişiliyor.
#   -> Matrisin son satırının son elemanına matris[-1, -1] ile erişiliyor.
# 6. Dilimleme: Diziden ilk 3 eleman dizi[0:3] ile seçiliyor ve yazdırılıyor.
# 7. Alt Matris Oluşturma: 0 ve 1. satır ile 1 ve 2. sütunları seçilerek alt_matris oluşturuluyor.