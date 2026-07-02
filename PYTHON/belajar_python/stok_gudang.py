print("=====STOK GUDANG=====")

with open("stok_gudang.txt", "w") as file: 

    while True:
        nama_barang = input("masukkan nama barang(enter untuk selesai): ")
        if nama_barang == "":
            break
        
        jumlah_barang = int(input("masukkan jumlah:"))
        stok_gudang = int(input("masukkan jumlah yang diambil: "))

        if stok_gudang > jumlah_barang:
            print("stok tidak cukup")

        sisa_stok = jumlah_barang - stok_gudang
        jumlah = str(sisa_stok)

        file.write(nama_barang + "=" + jumlah + "\n")
        print("data",jumlah,"berhasil disimpan")

file.close()
print("program selesai")