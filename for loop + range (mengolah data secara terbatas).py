# Proyek input data pakai for loop(terbatas)
print("---masukkan 5 harga produk digital lynk---")
total = 0
for i in range(5):
    harga_produk = int(input(f"Masukkan harga produk lynk-mu ke-{i+1}: ")) # i adalah nomor urutan dimulai dari 0
    total = total + harga_produk
    rata_rata = total // 5
    print("-" * 35)
print(f"\nTotal keuntungan dari 5 produk : Rp {total}")
print(f"rata-rata keuntungan per-produk : Rp {rata_rata}")