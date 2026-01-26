#1. Kita buat "resepnya" dulu (def-inisi fungsi)
def sapa_pegawai(nama, posisi):
    print(f"Halo {nama}")
    print(f"selamat bertugas sebagai {posisi} di kantor ini!")
    print("-" * 20)
    
#2. Program utama (tinggal panggil resepnya)
while True :
    nama_user = input("Masukkan nama pegawai (ketik 'stop' untuk selesai) : ")
    if nama_user.lower() == 'stop':
        break
        
    jabatan_user = input("Jabatan : ")
    
    # Memanggil fungsi
    sapa_pegawai(nama_user, jabatan_user)
    
print("Program selesai! sampai jumpa besok di pc!")