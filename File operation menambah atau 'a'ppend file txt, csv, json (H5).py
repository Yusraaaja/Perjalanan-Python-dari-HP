import os

nama_file = "database_pegawai.txt"

print("---Sistem Pencatat Data Permanen---")

while True:
    nama = input("\nNama pegawai (ketik 'exit' untuk keluar): ")
    if nama.lower() == 'exit':
        break
    
    jabatan = input("Jabatan: ")
    
    # Try-except paling cocok diletakkan di sini
    try:
        umur = int(input("Umur: "))
    except ValueError:
        print("Waduh! Umur harus angka bang, saya masukin 0 dulu ya.")
        umur = 0

    # Simpan ke file
    with open(nama_file, "a") as file:
        file.write(f"Nama: {nama} | Jabatan: {jabatan} | Umur: {umur}\n")
    
    print(f"Selesai! Data {nama} berhasil diamankan kedalam {nama_file}")

print(f"\nProgram selesai, silakan cek folder tempat kamu simpan {nama_file}")