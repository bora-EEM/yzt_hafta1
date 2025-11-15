import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

basket = pd.read_csv('basket_details.csv')
customer = pd.read_csv('customer_details.csv')

df = pd.merge(
    left = basket,
    right = customer,
    on = 'customer_id',
    how = 'inner'
)
#df['basket_date'] = pd.to_datetime(df['basket_date'])
print(basket.head())
print(customer.head())
print(df.head())
print(df.info())

#görselleştirme
df['basket_date'] = pd.to_datetime(df['basket_date'])
df_zaman = df.set_index('basket_date')
aylik_satislar = df_zaman['basket_count'].resample('D').sum()

plt.figure(figsize=(14, 6))

# Çizgi grafiği oluştur
plt.plot(
    aylik_satislar.index,
    aylik_satislar.values,
)

# Grafik Başlıkları ve Eksen Ayarları
plt.title('Aylık Satış Performansı (Toplam Satılan Ürün Adedi)', fontsize=16)
plt.xlabel('Tarih (Ay)', fontsize=12)
plt.ylabel('Satılan Toplam Ürün Adedi', fontsize=12)
plt.show()

#ürün satış adetleri
urun_satis_adetleri = df.groupby('product_id')['basket_count'].sum()
en_populer_10 = urun_satis_adetleri.sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
en_populer_10.plot(kind='bar', color='darkgreen')
plt.title('En Popüler 10 Ürün (Toplam Satılan Adet)', fontsize=16)
plt.xlabel('Ürün ID', fontsize=12)
plt.ylabel('Toplam Satış Adedi', fontsize=12)
plt.show()