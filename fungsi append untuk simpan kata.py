# kalkulator versi 'huruf', menyimpan data, lalu tampilkan dengan for loop
list_barang = []
print("---Masukkan nama barang---")
print("ketik 'selesai' untuk menutup program")

while True :
    nama = input("Masukkan nama barang : ")
    print("-" * 35)
    if nama_barang == 'selesai' :
        break
     
     list_barang.append(nama)
     
print(f"nama barang {list_barang}")