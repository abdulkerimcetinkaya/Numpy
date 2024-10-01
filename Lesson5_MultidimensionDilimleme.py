import numpy as np

dizi = np.array([10,20,30,40,50])
d_eleman = dizi[2]
# print(d_eleman)

matris = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matris)
m_eleman = matris[2,2]
# print(m_eleman)

print("Dizi'nin Son Elemanı : ", dizi[-1])
print("Matris'in Son Satırın Son Elemanı : ", matris[-1,-1])

dilim = dizi[0:3]
print("Dilim : ", dilim)

alt_matris = matris[0:2,1:3]
print(alt_matris)