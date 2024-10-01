import numpy as np

# Tek boyutlu bir NumPy dizisi oluşturuluyor
dizi = np.array([10, 20, 30, 40, 50])

# Dizinin 3. elemanını seçiyor (0 tabanlı indeksleme ile 2. indeks)
d_eleman = dizi[2]
# print(d_eleman)  # Ekrana yazdırmak için kullanılabilir

# 2 boyutlu bir NumPy matrisi oluşturuluyor
matris = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
# print(matris)  # Matrisi ekrana yazdırmak için kullanılabilir

# Matrisin 3. satır ve 3. sütunundaki elemanı (2,2 indeksli eleman)
m_eleman = matris[2, 2]
# print(m_eleman)  # Bu elemanı ekrana yazdırmak için kullanılabilir

# Dizinin son elemanına negatif indeksleme ile erişiliyor
print("Dizi'nin Son Elemanı : ", dizi[-1])

# Matrisin son satırının son elemanına negatif indeksleme ile erişiliyor
print("Matris'in Son Satırın Son Elemanı : ", matris[-1, -1])

# Diziden ilk 3 elemanı (0'dan 3. indeksine kadar) dilimleme ile seçiyor
dilim = dizi[0:3]
print("Dilim : ", dilim)

# Matristen 0. ve 1. satır ile 1. ve 2. sütunu seçerek bir alt matris oluşturuluyor
alt_matris = matris[0:2, 1:3]
print("Alt Matris: \n", alt_matris)
