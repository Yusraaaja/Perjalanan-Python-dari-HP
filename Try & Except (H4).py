# Try - Except
while True :
    try :
        harga = int(input("Masukkan harga produk (angka saja) : "))
        print(f"harga tersimpan : Rp {harga}")
        break # loop berhenti kalau input benar
    except ValueError :
        print("Waduh! Masukkan angka aja ya, jangan pake huruf!")