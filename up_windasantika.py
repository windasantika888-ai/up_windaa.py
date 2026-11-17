# Aplikasi Pemesanan Tiket Bioskop CINEMA

print("=== CINEMA - Pemesanan Tiket Bioskop ===")

while True:
    # 1. Input Nama Pelanggan
    nama = input("\nMasukkan nama pelanggan : ")

    # 2. Input Jenis dan Jumlah Tiket
    print("\nJenis Tiket:")
    print("1. Regular - Rp 35.000")
    print("2. VIP - Rp 50.000")
    print("3. Premium - Rp 75.000")
    pilihan = input("Pilih jenis tiket (1/2/3) : ")
    jumlah = int(input("Masukkan jumlah tiket : "))

    # 3. Tentukan Harga 
    if pilihan == "1":
        jenis = "Regular"
        harga = 35000
    elif pilihan == "2":
        jenis = "VIP"
        harga = 50000
    elif pilihan == "3":
        jenis = "Premium"
        harga = 75000
    else:
        print("Pilihan tidak valid!")
        continue

    total_awal = harga * jumlah

    # 4. Cek Diskon 
    if jumlah > 3:
        diskon = total_awal * 0.10
        keterangan = "Dapat Diskon 10%"
    else:
        diskon = 0
        keterangan = "Tidak Dapat Diskon"

    total_bayar = total_awal - diskon

    # Tampilkan Struk
    print("\n--- STRUK PEMBAYARAN ---")
    print(f"Nama Pelanggan : {nama}")
    print(f"Jenis Tiket    : {jenis}")
    print(f"Harga Tiket    : Rp {harga}")
    print(f"Jumlah Tiket   : {jumlah}")
    print(f"Total Awal     : Rp {total_awal}")
    print(f"Diskon         : Rp {diskon} ({keterangan})")
    print(f"Total Bayar    : Rp {total_bayar}")
    print("------------------------")

    # 5. Proses Berulang
    lagi = input("\nAda pelanggan lagi? (y/n) : ")
    if lagi.lower() != "y":
        print("\nTerima kasih! Program selesai.")
        break