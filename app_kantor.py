import os

# Nama file tempat menyimpan  data
nama_file = "database_pegawai.txt"

print("---Sistem Pencatat Data Permanen---")

while True :
    nama = input("\nNama pegawai (ketik 'exit' untuk keluar) : ")
    if nama.lower() == 'exit' :
            break
    
    jabatan = input("Jabatan : ")
    
    try :
        umur = int(input("Umur : "))
    except ValueError :
        print("Masukkan angka aja ya, jangan pakai huruf!")
        umur = 0

    # Proses menyimpan ke file (mode 'a' artinya append/menambah)   
    with open(nama_file, "a") as file :
        file.write(f"Nama: {nama} | Jabatan: {jabatan} | Umur: {umur}\n")

    print(f"Selesai! Data {nama} berhasil diamankan kedalam {nama_file}")
print(f"\nProgram selesai, silahkan cek folder tempat kamu simpan {nama_file}, nanti akan ada file '.txt' silahkan cek!")