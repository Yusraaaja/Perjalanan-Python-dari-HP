target_laptop = int(input('berapa harga laptop yang mau kamu beli? : '))
harga_jual = int(input('berapa harga produk lynk-mu? : '))

# Menggunakan pembagian bulat (//) agar hasilnya tidak ada .0
jumlah_terjual = target_laptop // harga_jual

# Menggunakan f-string (huruf f didepan tanda string) agar kode jadi lebih rapi
print(f'target duit yang mau dikumpulin : Rp {target_laptop}')
print(f'berarti kamu harus jualan sebanyak {jumlah_terjual} produk buat beli laptop itu!')