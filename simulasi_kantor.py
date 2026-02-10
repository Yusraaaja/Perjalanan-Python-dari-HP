import pandas as pd

#1. load data kotor
df = pd.read_csv('data_kantor_kotor.csv')

print("---Data sebelum dibersihkan---")
print(df)

#2. bersihkan data (data cleaning)
# isi gaji yang kosong dengan rata-rata gaji yang ada
rata_gaji = df['Gaji'].mean()
df['Gaji'] = df['Gaji'].fillna(rata_gaji)

#isi departemen yang kosong dengan "General"
df['Departemen'] = df['Departemen'].fillna('General')

#3. automation: Tambah pajak 5%
df['Pajak'] = df['Gaji'] * 0.05
df['Gaji_Bersih'] = df['Gaji'] - df['Pajak']

print("\n--- Data setelah dibersihkan ---")
print(df)

#4. export ke excel
df.to_excel('Laporan_keuangan_bersih.xlsx', index=False)
print("\n Laporan professional telah siap di 'Laporan_keuangan_bersih.xlsx'!")