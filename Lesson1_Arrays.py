import numpy as np

dizi = np.array([1,2,3,4,5])
print(dizi)

dizi2 = np.arange(0,10,2)
print(dizi2)

dizi3 = np.linspace(0,2,5)
print(dizi3)


boyut= dizi.ndim
veri_tipi = dizi.dtype
print("Dizinin Boyutu : ", boyut)
print("Dizinin Tipi : ", veri_tipi)
