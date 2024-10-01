import numpy as np

# 2 boyutlu bir NumPy dizisi oluşturuluyor. İlk satır gün adlarını, ikinci satır sayıları içeriyor.
dizi = np.array([["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"], 
                 [6, 7, 8, 9, 10]])
# İlk diziyi ekrana yazdırıyor
print(dizi)

# Çıktı arasında bir ayrım olması için 45 karakter uzunluğunda "-" yazdırılıyor
print("-" * 45)

# 3 boyutlu bir NumPy dizisi oluşturuluyor. İlk satır ay adlarını, ikinci ve üçüncü satır sayıları içeriyor.
dizi2 = np.array([["Ocak", "Şubat", "Mart", "Nisan", "Mayıs"], 
                  [6, 7, 8, 9, 10], 
                  [11, 12, 13, 14, 15]])
# İkinci diziyi ekrana yazdırıyor
print(dizi2)
