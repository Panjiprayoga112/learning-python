stok_gudang = {}

with open("stok_gudang.txt", "w") as file:

while True:
    print("1.masukan nama barang: ")
    print("2.masukan jumlah barang: ")
    print("3.masukkan pengurangan barang: ")
    print("4.tampilkan stok barang: ")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nama_barang = input("Masukan nama barang: ")
        jumlah_barang = int(input("Masukan jumlah barang: "))
        stok_gudang[nama_barang] = stok_gudang.get(nama_barang, 0) + jumlah_barang
        print(f"Stok {nama_barang} berhasil ditambahkan. Total stok: {stok_gudang[nama_barang]}")

    elif pilihan == "2":
        nama_barang = input("Masukan nama barang: ")
        jumlah_barang = int(input("Masukan jumlah barang: "))
        if nama_barang in stok_gudang:
            stok_gudang[nama_barang] += jumlah_barang
            print(f"Stok {nama_barang} berhasil ditambahkan. Total stok: {stok_gudang[nama_barang]}")
        else:
            print(f"Barang {nama_barang} tidak ditemukan di gudang.")

    elif pilihan == "3":
        nama_barang = input("Masukkan nama barang: ")
        jumlah_pengurangan = int(input("Masukkan jumlah pengurangan barang: "))
        if nama_barang in stok_gudang:
            if stok_gudang[nama_barang] >= jumlah_pengurangan:
                stok_gudang[nama_barang] -= jumlah_pengurangan
                print(f"Stok {nama_barang} berhasil dikurangi. Total stok: {stok_gudang[nama_barang]}")
            else:
                print(f"Stok {nama_barang} tidak cukup untuk dikurangi.")
        else:
            print(f"Barang {nama_barang} tidak ditemukan di gudang.")

    elif pilihan == "4":
        print("Stok Barang di Gudang:")
        for barang, jumlah in stok_gudang.items():
            print(f"{barang}: {jumlah}")

    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-4.")


file.close()print("Program selesai.")

