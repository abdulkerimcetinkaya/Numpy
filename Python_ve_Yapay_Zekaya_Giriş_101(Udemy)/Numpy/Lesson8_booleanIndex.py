import numpy as np

dizi = np.array([100,25,38,49,56,78,52,65,85])
boolean_mask = dizi > 50
print(boolean_mask)

selected = dizi[boolean_mask]
print("50 den büyük elemanlar", selected)

boolean_mask = (dizi > 30) & (dizi < 70)
print("30 ile 70 arasında ki elemanlar ", dizi[boolean_mask])