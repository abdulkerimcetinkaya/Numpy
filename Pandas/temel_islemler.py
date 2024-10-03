import pandas as pd  # Pandas kütüphanesini içe aktarma

# Bir pandas Series oluşturma
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
# Series'i ekrana yazdırma (şu an yorum satırında)
# print(s)

# Bir sözlük oluşturma
data = {
    'Fiyat': [45, 85, 74, 12],  # Fiyat bilgileri
    'Satış Adedi': [2, 5, 7, 30],  # Satış adedi bilgileri
    'Kategori': ['Roman', 'Bilim', 'Çocuk', 'Tarih']  # Kategori bilgileri
}

# Sözlükten bir DataFrame oluşturma
df = pd.DataFrame(data)
# DataFrame'i ekrana yazdırma (şu an yorum satırında)
# print(df)
# DataFrame'in ilk 2 satırını ekrana yazdırma (şu an yorum satırında)
# print(df.head(2))
# DataFrame hakkında bilgi ekrana yazdırma (şu an yorum satırında)
# print(df.info())
# DataFrame'in istatistiksel özetini ekrana yazdırma (şu an yorum satırında)
# print(df.describe())

# Fiyat ve Kategori sütunlarını ekrana yazdırma (şu an yorum satırında)
# print(df[['Fiyat', 'Kategori']])

# Fiyatı 50'den büyük olan satırları filtreleme
filter = df[df['Fiyat'] > 50]
# Filtrelenen satırları ekrana yazdırma (şu an yorum satırında)
# print(filter)

# Yeni bir sütun ekleme: Toplam Gelir
df['Toplam Gelir'] = df['Fiyat'] * df['Satış Adedi']
# Güncellenmiş DataFrame'i ekrana yazdırma
print(df)

# Kategori sütununu silme
df = df.drop('Kategori', axis=1)
# Güncellenmiş DataFrame'i ekrana yazdırma
print(df)
