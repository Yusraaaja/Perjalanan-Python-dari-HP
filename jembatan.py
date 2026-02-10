import pandas as pd

def proses_data_custom():
    try:
        with open('database_pegawai.txt', 'r') as f:
            baris_data = f.readlines()

        data_bersih = []
        for baris in baris_data:
            #memisahkan berdasarkan tanda '|'
            bagian = baris.split('|')
            #mengambil nilai setelah tanda ':' dan menghapus spasi
            nama = bagian[0].split(':')[1].strip()
            jabatan = bagian[0].split(':')[1].strip()
            umur = bagian[0].split(':')[1].strip()

            data_bersih.append({'Nama': nama, 'Jabatan': jabatan, 'Umur': umur})

        #2. ubah menjadi dataframe
        df = pd.DataFrame(data_bersih)

        #3. simpan ke excel (karena tidak ada gaji, kita simpan data yang ada saja)
        df.to_excel('Laporan_final_pegawai.xlsx', index=False)
        print("Script berhasil membedah isi database_pegawai.txt!")
        print(df)

    except Exception as e:
        print(f"Ada masalah lain: {e}")

proses_data_custom()