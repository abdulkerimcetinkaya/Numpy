import numpy as np

# Bir NumPy dizisi oluşturuluyor
dizi = np.array([1, 2, 3, 4, 5])
# İlk diziyi ekrana yazdırıyor
print(dizi)

# Belirli bir aralıktan (0 dahil, 10 hariç) 2 adımlık artışlarla bir dizi oluşturuluyor
dizi2 = np.arange(0, 10, 2)
# İkinci diziyi ekrana yazdırıyor
print(dizi2)

# 0 ile 2 arasında eşit aralıklarla 5 elemanlı bir dizi oluşturuluyor
dizi3 = np.linspace(0, 2, 5)
# Üçüncü diziyi ekrana yazdırıyor
print(dizi3)

# İlk dizinin boyutunu (kaç boyutlu olduğunu) öğrenmek için ndim özelliği kullanılıyor
boyut = dizi.ndim
# İlk dizinin elemanlarının veri tipini öğrenmek için dtype özelliği kullanılıyor
veri_tipi = dizi.dtype
# Dizinin boyutunu ekrana yazdırıyor
print("Dizinin Boyutu : ", boyut)
# Dizinin elemanlarının veri tipini ekrana yazdırıyor
print("Dizinin Tipi : ", veri_tipi)
