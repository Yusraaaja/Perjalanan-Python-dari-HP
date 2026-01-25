# Cara jitu mengolah banyak data sekaligus tanpa batas
daftar_harga = [] # Wadah menyimpan data
print("---Input Harga Sepuasnya---")
print("Ketik '0' jika sudah selesai meng-input untuk melihat total. \n")

while True :
    harga = int(input("Masukkan harga produk : "))
    print("-" * 30)
    if harga == 0 :
        break # berhenti jika user input 0
        
    daftar_harga.append(harga) # memasukkan data ke dalam daftar harga tanpa batas

# setelah loop berhenti, kita olah datanya
total = sum(daftar_harga) # fungsi otomatis untuk menjumlahkan semua harga (total)
jumlah_data = len(daftar_harga) # menghitung ada berapa banyak input yang masuk

print(f"total keuntungan : Rp {total}")
print(f"banyak produk : {jumlah_data}")
print(f"rata-rata : Rp {total // jumlah_data}")