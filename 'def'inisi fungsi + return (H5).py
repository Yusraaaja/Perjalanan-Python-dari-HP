# 1. Fungsi untuk menghitung bonus gaji (Logika Arsitek)
def hitung_bonus(jabatan, gaji_pokok):
    if jabatan.lower() == "manager" :
        bonus = gaji_pokok * 0.5 # Bonus 50%
    elif jabatan.lower() == "staff" :
        bonus = gaji_pokok * 0.2 # Bonus 20%
    else :
        bonus = gaji_pokok * 0.1 # Bonus 10%
        
    return bonus # ini kuncinya! Mengirim hasil keluar fungsi.
        
#--- Program Utama ---
nama = input("nama pegawai : ")
jabatan = input("jabatan (manager/staff/lainnya) : ")
gaji_pokok = int(input("gaji pokok : "))

# Kita panggil fungsinya dan simpan hasilnya di variabel baru
hasil_bonus = hitung_bonus(jabatan, gaji_pokok)

total_gaji = gaji_pokok + hasil_bonus

print(f"\n---Rincian Gaji {nama}---")
print(f"gaji pokok : Rp{gaji_pokok}")
print(f"bonus gaji : Rp{hasil_bonus}")
print(f"total gaji : Rp{total_gaji}")