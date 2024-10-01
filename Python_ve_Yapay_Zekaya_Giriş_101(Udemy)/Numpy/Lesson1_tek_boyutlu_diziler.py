import numpy as np

# NumPy dizisi oluşturma
dizi1 = np.array([1, 2, 3, 4, 5])
# İlk diziyi ekrana yazdırma
print(dizi1)

# 0 ile 10 arasında (10 hariç), 2 adımlık bir aralıkla bir dizi oluşturma
dizi2 = np.arange(0, 10, 2)
# İkinci diziyi ekrana yazdırma
print(dizi2)

# 0 ile 2 arasında eşit aralıklarla 5 elemanlı bir dizi oluşturma
dizi3 = np.linspace(0, 2, 5)
# Üçüncü diziyi ekrana yazdırma
print(dizi3)

# İlk dizinin boyutunu alma
boyutlar = dizi1.ndim
# İlk dizinin elemanlarının veri tipini alma
veri_tipi = dizi1.dtype
# Dizinin boyut sayısını ekrana yazdırma
print("Boyut Sayısı:", boyutlar)
# Dizinin elemanlarının veri tipini ekrana yazdırma
print("Veri Tipi:", veri_tipi)
