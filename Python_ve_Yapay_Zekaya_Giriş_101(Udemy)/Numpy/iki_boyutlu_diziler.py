import numpy as np

# 2 boyutlu bir NumPy dizisi oluşturuluyor. İlk satır gün adlarını, ikinci satır sayıları içeriyor.
gunler_ve_sayilar = np.array([["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"],
                              [6, 7, 8, 9, 10]])
# İlk diziyi ekrana yazdırma
print(gunler_ve_sayilar)

# Açıklık için 45 karakter uzunluğunda bir ayırıcı satır yazdırma
print("-" * 45)

# 3 boyutlu bir NumPy dizisi oluşturuluyor. İlk satır ay adlarını, ikinci ve üçüncü satır sayıları içeriyor.
aylar_ve_sayilar = np.array([["Ocak", "Şubat", "Mart", "Nisan", "Mayıs"],
                              [6, 7, 8, 9, 10],
                              [11, 12, 13, 14, 15]])
# İkinci diziyi ekrana yazdırma
print(aylar_ve_sayilar)


# -> Kod, gün adlarını ve bunlara karşılık gelen sayıları içeren gunler_ve_sayilar adlı 2 boyutlu bir NumPy dizisi oluşturur.
# -> Bu diziyi yazdırdıktan sonra, açıklık sağlamak için 45 karakter uzunluğunda bir ayırıcı satır ekler.
# -> Ardından, ay adlarını ve karşılık gelen sayıları içeren aylar_ve_sayilar adlı 3 boyutlu bir NumPy dizisi oluşturur.
# -> Son olarak, bu ikinci diziyi de yazdırır.