import pandas as pd

def buat_database_excel():
    print("--- PROGRAM PENGOLAH DATA PEGAWAI ---")
    
    # 1. Menyiapkan data (Simulasi input banyak data)
    data_mentah = {
        'Nama': ['Yusra', 'Jordan', 'Sonia', 'Alva'],
        'Jabatan': ['Architect', 'Manager', 'Staff', 'DevOps'],
        'Gaji_Pokok': [9000000, 5000000, 3000000, 7000000]
    }

    # 2. Mengubah ke DataFrame (Tabel Pandas)
    df = pd.DataFrame(data_mentah)

    # 3. AUTOMATION: Menghitung Bonus 10% dan Total Gaji secara instan
    df['Bonus'] = df['Gaji_Pokok'] * 0.1
    df['Total_Gaji'] = df['Gaji_Pokok'] + df['Bonus']

    # 4. EXPORT: Menyimpan ke file Excel nyata
    nama_file = 'Laporan_Gaji_Januari.xlsx'
    df.to_excel(nama_file, index=False)
    
    print("\n" + "="*30)
    print(f"✅ BERHASIL! File '{nama_file}' sudah dibuat.")
    print("="*30)
    print(df) # Menampilkan tabel di terminal

# Jalankan fungsinya
buat_database_excel()