nama_file = "database_pengawal.txt"

print("---Sistem Pencari Data---")
cari = input("Masukkan nama pegawai yang ingin dicari: ")
ketemu = False

try :
    with open(nama_file, "r") as file :
        baris_data = file.readlines()

        print("\nHasil pencarian : ")
        for baris in baris_data :
            if cari.lower() in baris.lower():
                print(f"Ditemukan -> {baris.strip()}")
                ketemu = True

        if not ketemu:
            print(f"Maaf data dengan nama {cari} tidak ditemukan.")

except FileNotFoundError :
    print("Wah, filenya belum lu buat we, buat dulu dah!")