database_pegawai = [] # list untuk menampung banyak dictionary

print("---Sistem Input Data Pegawai Kantor Bupati---")

while True :
    nama = input("\nMasukkan Nama (Ketik 'selesai' untuk stop) : ")
    if nama.lower() == 'selesai' :
        break
        
    jabatan = input("Masukkan Jabatanmu : ")
    umur = int(input("Masukkan Umurmu : "))
    
    # Bungkus data dalam dictionary
    data_baru = {
        "nama" : nama,
        "jabatan" : jabatan,
        "umur" : umur
    }
    # Masukkan dictionary ke dalam list database
    database_pegawai.append(data_baru)
    
# Menampilkan hasil akhirnya
print("\n" + "+" * 35)
print("REKAP DATA PEGAWAI")
print("=" * 35)

for pegawai in database_pegawai :
    print(f"Nama Pegawai : {pegawai['nama']} | Jabatan : {pegawai['jabatan']} | Umur : {pegawai['umur']}")