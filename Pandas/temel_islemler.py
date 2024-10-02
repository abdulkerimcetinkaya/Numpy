import pandas as pd

s = pd.Series([10,20,30,40], index=["a","b","c","d"])
# print(s)

data = {
    'Fiyat':[45,85,74,12],
    'Satış Adedi':[2,5,7,30],
    'Kategori':['Roman', 'Bilim', 'Çocuk', 'Tarih']
}


df = pd.DataFrame(data)
# print(df)
# print(df.head(2))
# print(df.info())
# print(df.describe())

# print(df[['Fiyat','Kategori']])
filter = df[df['Fiyat'] > 50]
# print(filter)

# Satır ekleme
df['Toplam Gelir'] = df['Fiyat'] * df['Satış Adedi']
print(df)

# Satır Silme
df = df.drop('Kategori', axis=1)
print(df)
