nama_file = "database_pegawai.txt"

print("--- SISTEM PENCARIAN DATA PEGAWAI ---")
cari = input("Masukkan nama pegawai yang ingin dicari: ")
ketemu = False

try:
    with open(nama_file, "r") as file: # "r" artinya READ (Membaca)
        baris_data = file.readlines()
        
        print("\nHasil Pencarian:")
        for baris in baris_data:
            if cari.lower() in baris.lower():
                print(f"🔍 Ditemukan -> {baris.strip()}")
                ketemu = True
        
        if not ketemu:
            print(f"❌ Maaf, data dengan nama '{cari}' tidak ada.")

except FileNotFoundError:
    print("Wah, filenya belum dibuat bang! Jalankan dulu program inputnya.")