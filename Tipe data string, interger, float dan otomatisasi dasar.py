# 1. Data Bisnis Lynk (Tipe data & Interger)
nama_produk = 'Resep makanan 10 menit' # String
harga_produk = 30000 # Interger
status_produk = 'ada'  # Boolean

# 2. Data PKL Kantor Bupati (Tipe data string & float)
nama_pegawai = 'Nolan'
uang_tunjangan = 1500.50 # float

# 3. Menampilkan Data 
print('info produk lynk')
print('produk : ', nama_produk)
print('harga : Rp', harga_produk)
print('kesediaan : ', status_produk)

print('\n---info pegawai pemkab---')
print('Nama : ', nama_pegawai)
print('Tunjangan : $', uang_tunjangan)

# Perhitungan otomatis (otomatisasi dasar)
pajak_lynk = harga_produk * 0.05
total_terima = harga_produk - pajak_lynk
print('\nPotongan Admin lynk (5%) : Rp', pajak_lynk)
print('keuntungan bersih : Rp', total_terima)