import numpy as np

data = np.loadtxt('data.txt', delimiter=' ')

row_sums = np.sum(data , axis=1)
# print("Her satırın toplamı :", row_sums)

# np.savetxt('output.txt', row_sums , fmt='%d')

output_data = np.column_stack((data, row_sums))

np.savetxt('output_with_sums.txt', output_data, fmt='%d' , delimiter=' ')
print('Kayıt işlemi tamamlandı !')
