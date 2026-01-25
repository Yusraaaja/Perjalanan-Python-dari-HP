# for loop
menus = ["nasi goreng","soto", "bakso"]
print("---Daftar menu di lynk saya---")
for menu in menus :
    print(f"Menu : {menu}")
    
# while loop
print("\n---Sistem input pegawai---")
while True :
    nama = input("Masukkan nama pegawai (Ketik 'stop' untuk keluar) : ")
    if nama == 'stop' :
        break
    elif nama.isalpha() :
        print(f"pegawai {nama} berhasil di data!")
    else :
        print("Nama tidak valid. Mohon masukkan dengan benar.")
    
print("Program selesai. Semua data berhasil tersimpan.")