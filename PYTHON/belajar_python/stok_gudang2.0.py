print("===== STOK GUDANG =====")

with open("stok_gudang.txt", "w") as file:

    while True:
        nama_barang = input("Masukkan nama barang (Enter untuk selesai): ")
        if nama_barang == "":
            break

        jumlah_barang = int(input("Masukkan jumlah barang: "))
        jumlah_diambil = int(input("Masukkan jumlah yang diambil: "))

        if jumlah_diambil > jumlah_barang:
            print("Stok tidak cukup!")
            continue

        sisa_stok = jumlah_barang - jumlah_diambil

        file.write(nama_barang + "=" + str(sisa_stok) + "\n")
        print("Data", sisa_stok, "berhasil disimpan")

print("Program selesai")