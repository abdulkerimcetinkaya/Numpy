import numpy as np

# İki adet bir boyutlu NumPy dizisi oluşturuluyor
dizi1 = np.array([1, 2, 3])
dizi2 = np.array([4, 5, 6])

# İki bir boyutlu diziyi birleştiriyoruz
birlesik_dizi = np.concatenate((dizi1, dizi2))
print("Bir boyutlu diziler birleştirildi:", birlesik_dizi)

# İki adet iki boyutlu NumPy dizisi oluşturuluyor
dizi1_2d = np.array([[1, 2, 3], [4, 5, 6]])
dizi2_2d = np.array([[7, 8, 9], [10, 11, 12]])

# İki boyutlu dizileri dikey olarak birleştiriyoruz
birlesik_dizi_dikey = np.vstack((dizi1_2d, dizi2_2d))
print("Dikey olarak birleştirilen diziler:\n", birlesik_dizi_dikey)

# İki boyutlu dizileri yatay olarak birleştiriyoruz
birlesik_dizi_yatay = np.hstack((dizi1_2d, dizi2_2d))
print("Yatay olarak birleştirilen diziler:\n", birlesik_dizi_yatay)

# Bölme işlemi için bir boyutlu bir dizi oluşturuluyor
dizi_bol = np.array([1, 2, 3, 4, 5, 6])

# Bir boyutlu diziyi 3 parçaya bölüyoruz
bolunmus_diziler = np.split(dizi_bol, 3)
print("Bölünmüş bir boyutlu dizi:", bolunmus_diziler)

# Dikey ve yatay bölme işlemleri için iki boyutlu bir dizi oluşturuluyor
dizi_2d_bol = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# İki boyutlu diziyi dikey olarak 2 parçaya bölüyoruz
dikey_bolme = np.vsplit(dizi_2d_bol, 2)
print("Dikey olarak bölünmüş iki boyutlu dizi:", dikey_bolme)

# İki boyutlu diziyi yatay olarak 2 parçaya bölüyoruz
yatay_bolme = np.hsplit(dizi_2d_bol, 2)
print("Yatay olarak bölünmüş iki boyutlu dizi:", yatay_bolme)


# 1. Bir Boyutlu Dizi Oluşturma: dizi1 ve dizi2 adında iki bir boyutlu dizi oluşturulur.
# 2. Dizi Birleştirme:
#   -> birlesik_dizi: dizi1 ve dizi2 birleştirilir.
# 3. İki Boyutlu Dizi Oluşturma: dizi1_2d ve dizi2_2d adında iki iki boyutlu dizi oluşturulur.
# 4. Dikey ve Yatay Birleştirme: dizi1_2d ve dizi2_2d hem dikey hem de yatay olarak birleştirilir.
# 5. Dizi Bölme:
#   -> dizi_bol: Bir boyutlu dizi 3 parçaya bölünür.
#   -> dizi_2d_bol: İki boyutlu dizi hem dikey hem de yatay olarak 2 parçaya bölünür.