nama_buah = ["pisang", "manga", "apel"]

for buah in nama_buah:
    print(buah)

for i in range (0, len(nama_buah)):
    print(nama_buah[i])

tebak_buah = input("masukkan nama buah: ")

if tebak_buah in nama_buah:
    print(f"{tebak_buah} tebakan anda benar")

else:
    print(f"{tebak_buah} tebakan anda salah")