import numpy as np

# 1D NumPy dizisi oluşturma
orijinal_dizi = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# Diziyi 2x6 boyutunda matris olarak yeniden şekillendirme
yeniden_sekillendirilmis_dizi = orijinal_dizi.reshape((2, 6))  # 12 eleman olduğu için (2, 6) olarak değiştirildi
otomatik_boyut = -1  # Bu, diğer boyutlara göre otomatik olarak şekli belirleyecektir
print("Orijinal Dizi:\n", orijinal_dizi)
print("Yeniden Şekillendirilmiş Dizi (2x6):\n", yeniden_sekillendirilmis_dizi)

# 2D NumPy matris oluşturma
matris = np.array([[1, 2], [3, 4], [5, 6]])
# Matrisi 1D diziye yeniden şekillendirme
bir_d_array = matris.reshape(-1)
print("Matristen Oluşan 1D Dizi:\n", bir_d_array)

# Orijinal diziyi otomatik sütun belirlemesi ile 3 satırlık diziye yeniden şekillendirme
yeniden_sekillendirilmis_dizi_3_satir = orijinal_dizi.reshape(3, otomatik_boyut)
print("Yeniden Şekillendirilmiş Dizi (3 Satır):\n", yeniden_sekillendirilmis_dizi_3_satir)

# Matristeki 1D diziyi yazdırma
print("Matristen Oluşan 1D Dizi:\n", bir_d_array)


# 1. Orijinal Dizi Oluşturma: orijinal_dizi adında bir 1D NumPy dizisi oluşturulur.
# 2. Diziyi Yeniden Şekillendirme: yeniden_sekillendirilmis_dizi adında, orijinal diziyi 2x6 boyutunda bir matrise yeniden şekillendirir.
# 3. Otomatik Boyut Belirleme: otomatik_boyut, diğer boyutlara göre otomatik olarak şekli belirlemek için kullanılır.
# 4. 2D Matris Oluşturma: matris adında 2D bir NumPy matrisi oluşturulur.
# 5. Matrisi 1D Diziye Yeniden Şekillendirme: bir_d_array adında, matrisin 1D diziye dönüşümünü sağlar.
# 6. 3 Satırlık Diziye Yeniden Şekillendirme: yeniden_sekillendirilmis_dizi_3_satir, orijinal diziyi otomatik sütun sayısıyla 3 satırlık bir diziye dönüştürür.