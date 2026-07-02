# daftar_kosong = []
# print(daftar_kosong)

# nama = ["Alice", "Bob", "Charlie"]
# print(nama)

# campuran = [1, "dua", 3.0, True]
# print(campuran) 

# buah = ["apel", "jeruk", "pisang"]
# print(buah[0])  # Output: apel
# print(buah[1])  # Output: jeruk 
# print(buah[2])  # Output: pisang

# warna = ["merah", "hijau", "biru"]
# print(warna)
# warna[1] = "kuning"
# warna[0] = "hitam"
# print(warna)

# buah = ["apel", "jeruk", "pisang"]
# print(buah)
# buah.append("mangga")
# print(buah)
# buah.insert(1, "anggur")
# print(buah)

banyak_buah = ["apel", "jeruk", "pisang", "mangga", "anggur"]

for buah in banyak_buah:
    print(buah)

for i in range(0, len(banyak_buah)):
    print(banyak_buah[i])

if "jeruk" in banyak_buah:
    print("Jeruk ada dalam daftar buah.")   
    
else:
    print("Jeruk tidak ada dalam daftar buah.")


nama_buah = input("Masukkan nama buah yang ingin dicari: ")

if nama_buah in banyak_buah:
    print(f"{nama_buah} ada dalam daftar buah.")    

else:
    print(f"{nama_buah} tidak ada dalam daftar buah.")    