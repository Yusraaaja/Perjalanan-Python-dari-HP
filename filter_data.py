import pandas as pd

#1. Baca file excel yang baru kamu buat tadi
df = pd.read.excel('Laporan_Gaji_Januari.xlsx')

#2. FILTER: Ambil hanya pegawai yang Total_Gaji > 5.000.000
df_high_salary = df[df['Total_Gaji'] > 5000000]

# 3. Tampilkan hasilnya
print("\n--- PEGAWAI DENGAN GAJI DI ATAS 5 JUTA ---")
print(df_high_salary)

# 4. SIMPAN: Hasil filter ini ke file Excel terpisah
df_high_salary.to_excel('Laporan_Gaji_Tinggi.xlsx', index=False)
print("\n✅ File khusus gaji tinggi sudah dibuat!")