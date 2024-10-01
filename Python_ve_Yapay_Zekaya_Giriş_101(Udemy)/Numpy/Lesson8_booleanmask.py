import numpy as np

# Çeşitli tam sayı değerleri içeren bir NumPy dizisi oluşturuluyor
sayilar = np.array([100, 25, 38, 49, 56, 78, 52, 65, 85])

# 50'den büyük olan değerler için bir boolean maskesi oluşturuluyor
mask_50_den_buyuk = sayilar > 50
print("50'den büyük değerler için boolean maskesi:", mask_50_den_buyuk)

# Boolean maskesini kullanarak 50'den büyük olan elemanlar seçiliyor
elemanlar_50_den_buyuk = sayilar[mask_50_den_buyuk]
print("50'den büyük elemanlar:", elemanlar_50_den_buyuk)

# 30 ile 70 arasındaki (30 dahil, 70 hariç) değerler için bir boolean maskesi oluşturuluyor
mask_30_ile_70_arasi = (sayilar > 30) & (sayilar < 70)
# Boolean maskesini kullanarak 30 ile 70 arasındaki elemanlar seçiliyor
elemanlar_30_ile_70_arasinda = sayilar[mask_30_ile_70_arasi]
print("30 ile 70 arasındaki elemanlar:", elemanlar_30_ile_70_arasinda)


# 1. Dizi Oluşturma: sayilar adında bir NumPy dizisi oluşturuluyor.
# 2. Boolean Maskesi Oluşturma:
#   -> mask_50_den_buyuk: Bu maske, dizideki her elemanın 50'den büyük olup olmadığını kontrol eder.
# 3. Seçim Yapma:
#   -> elemanlar_50_den_buyuk: Boolean maskesi kullanılarak, 50'den büyük olan elemanlar seçilir.
# 4. 30 ile 70 Arasındaki Değerler için Maske Oluşturma:
#   -> mask_30_ile_70_arasi: Bu maske, dizideki her elemanın 30'dan büyük ve 70'ten küçük olup olmadığını kontrol eder.
#   -> elemanlar_30_ile_70_arasinda: Boolean maskesi kullanılarak, 30 ile 70 arasındaki elemanlar seçilir.