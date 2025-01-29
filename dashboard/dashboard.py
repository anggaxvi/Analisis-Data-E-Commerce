import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load data github
# data = pd.read_csv("data_penjualan_ecommerce.csv")
data = pd.read_csv("https://raw.githubusercontent.com/anggaxvi/Analisis-Data-E-Commerce/refs/heads/main/dashboard/data_penjualan_ecommerce.csv")
data = data.rename(columns={
    'product_category_name': 'Kategori Produk', 
    'order_id': 'Jumlah Terjual', 
    'review_score': 'Avg. Rating'
})

st.title('Proyek Akhir: Analisis Data Penjualan Produk E-Commerce :sparkles:')

#visualisasi pertanyaan pertama
st.subheader('1. Kategori produk apa yang paling laku terjual pada E-Commerce?')

st.dataframe(data,800,200)
fig, ax = plt.subplots(figsize=(10, 4))
colors = ["#D3D3D3", "#72BCD4"]

sns.barplot(
    y = "Jumlah Terjual",
    x = "Kategori Produk",
    data=data.head(5).sort_values(by="Jumlah Terjual",ascending=False)
)

plt.title("Kategori Produk yang Paling Terjual", loc="center",fontsize=15)
plt.ylabel("order_count")
plt.xlabel("category_product")
plt.tick_params(axis='x', labelsize = 8)
st.pyplot(fig)

st.write('Dilihat dari data penjualan 72 kategori produk pada tabel diatas, dapat disimpulkan bahwa kategori produk yang paling laku terjual adalah cama_mesa_banho dengan jumlah terjual sebanyak 11.270')
st.markdown("<br><br>",True)




#visualisasi pertanyaan kedua
st.subheader('2.Apakah ada korelasi jumlah kategori produk terjual dengan rating produk?')

fig, ax = plt.subplots(figsize=(10, 4))
sns.scatterplot(
    y = "Avg. Rating",
    x = "Jumlah Terjual",
    data= data,
    hue="Avg. Rating",
)

plt.title("Hubungan Penjualan dengan Review Produk", loc="center",fontsize=15)
plt.ylabel("review_mean")
plt.xlabel("order_count")
plt.tick_params(axis='x', labelsize = 8)
st.pyplot(fig)

correlation = data['Jumlah Terjual'].corr(data['Avg. Rating'])
st.write("Nilai korleasi antara penjualan dan review produk : ",correlation)
st.write('')
st.write("Dari hasil perhitungan korlasi antara jumlah penjualan produk dengan review produk dapat disimpulkan bahwa kedua varibel tersebut tidak memiliki hubungan yang kuat, karena nilai korelasi mendekati nilai 0 ")

st.caption('Github @anggaxvi')
