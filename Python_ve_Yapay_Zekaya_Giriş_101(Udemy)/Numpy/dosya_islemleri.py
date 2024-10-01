import numpy as np

# 'data.txt' dosyasından verileri yükleme
veri = np.loadtxt('data.txt', delimiter=' ')

# Her satırın toplamını hesaplama
satir_toplamlari = np.sum(veri, axis=1)
# print("Her satırın toplamı :", satir_toplamlari)

# Satır toplamlarını 'output.txt' dosyasına kaydetme
# np.savetxt('output.txt', satir_toplamlari, fmt='%d')

# Satır toplamlarını orijinal verilere ekleme
cikis_verisi = np.column_stack((veri, satir_toplamlari))

# Sonuç verisini 'output_with_sums.txt' dosyasına kaydetme
np.savetxt('output_with_sums.txt', cikis_verisi, fmt='%d', delimiter=' ')
print('Kayıt işlemi tamamlandı!')


# 1. Veri Yükleme: np.loadtxt ile data.txt dosyasından veriler okunur ve boşluk (' ') ile ayrılmış veriler bir NumPy dizisi olarak veri değişkenine kaydedilir.
# 2. Satır Toplamları: np.sum ile her bir satırın toplamı hesaplanır. axis=1 parametresi, toplamların satır bazında hesaplanmasını sağlar.
# 3. Kaydetme İşlemi: Yorum satırı haline getirilmiş kodlar, satır toplamlarının ayrı bir dosyaya (output.txt) kaydedilmesini sağlar. İhtiyaç halinde bu satırın     yorumunu kaldırarak çalıştırabilirsiniz.
# 4. Satır Toplamlarını Ekleme: np.column_stack, orijinal verilere satır toplamlarını ekleyerek yeni bir dizi (cikis_verisi) oluşturur.
# 5. Sonuçları Kaydetme: np.savetxt, output_with_sums.txt dosyasına orijinal veriler ve satır toplamlarını yazar.
# 6. Tamamlanma Mesajı: Kayıt işleminin tamamlandığını bildiren bir mesaj yazdırılır.