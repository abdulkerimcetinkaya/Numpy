import numpy as np

# Tek boyutlu bir NumPy dizisi oluşturuluyor
sayi_dizisi = np.array([10, 20, 30, 40, 50])

# Dizinin 3. elemanına erişiliyor (0'dan başlayarak 2. indeks)
ucuncu_eleman = sayi_dizisi[2]
print("Üçüncü Eleman: ", ucuncu_eleman)

# 2 boyutlu bir NumPy matrisi oluşturuluyor
sayi_matrisi = np.array([[1, 2, 3], 
                         [4, 5, 6], 
                         [7, 8, 9]])
# Matrisi ekrana yazdırıyor
print("Matris: \n", sayi_matrisi)

# Matrisin 3. satır ve 3. sütunundaki (2,2) elemanı alınıyor
matris_elemani = sayi_matrisi[2, 2]
print("Matrisin 3. Satır ve 3. Sütundaki Eleman: ", matris_elemani)

# Dizinin son elemanına erişiliyor
son_eleman = sayi_dizisi[-1]
print("Dizinin Son Elemanı: ", son_eleman)

# Matrisin son satırının son elemanına erişiliyor
matris_son_eleman = sayi_matrisi[-1, -1]
print("Matrisin Son Satırın Son Elemanı: ", matris_son_eleman)

# Diziden ilk 3 eleman dilimleniyor
ilk_uc_eleman = sayi_dizisi[0:3]
print("İlk Üç Eleman: ", ilk_uc_eleman)
