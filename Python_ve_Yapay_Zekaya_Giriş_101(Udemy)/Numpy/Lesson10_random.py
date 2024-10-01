import numpy as np

# 1 ile 10 arasında rastgele 5 tam sayı üret
rastgele_tamsayilar = np.random.randint(1, 11, size=5)  # 10 dahil değildir, bu yüzden 11 kullanıyoruz
print("1 ile 10 arasında rastgele üretilen tam sayılar:", rastgele_tamsayilar)

# 0 ile 1 arasında rastgele 5 ondalık sayı üret
rastgele_ondaliklar = np.random.random(5)
print("Rastgele üretilen ondalık sayılar:", rastgele_ondaliklar)

# Normal dağılımdan (ortalama 0, standart sapma 1) 5 rastgele sayı üret
normal_dagilim_sayilari = np.random.normal(0, 1, 5)
print("Normal dağılımdan rastgele sayılar:", normal_dagilim_sayilari)

# 0 ile 10 arasında rastgele tam sayılardan oluşan 3x3 dizi oluştur
rastgele_dizi = np.random.rand(3, 3) * 10  # 0 ile 10 arasında rastgele ondalık sayılar üret
rastgele_dizi = rastgele_dizi.astype(int)  # Tam sayıya dönüştür
print("3x3 boyutunda rastgele tam sayılardan oluşan dizi:\n", rastgele_dizi)


# 1. Rastgele Tam Sayı Üretimi: rastgele_tamsayilar adında 1 ile 10 arasında (10 dahil değil) 5 rastgele tam sayı üretilir.
# 2. Rastgele Ondalık Sayı Üretimi: rastgele_ondaliklar adında 0 ile 1 arasında 5 rastgele ondalık sayı üretilir.
# 3. Normal Dağılımdan Rastgele Sayı Üretimi: normal_dagilim_sayilari adında ortalaması 0 ve standart sapması 1 olan normal dağılımdan 5 rastgele sayı üretilir.
# 4. 3x3 Boyutunda Rastgele Dizi Oluşturma: rastgele_dizi adında 0 ile 10 arasında rastgele ondalık sayılardan oluşan bir 3x3 dizi oluşturulur ve bu dizi tam sayılara dönüştürülür.