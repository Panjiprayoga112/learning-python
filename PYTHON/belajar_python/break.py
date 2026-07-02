angka_rahasia = 7

# while True:
#     tebakan = int(input("masukkan angka: "))

#     if tebakan == angka_rahasia:
#         print("tebakan anda benar")
#         break
#     else:
#         print("tebakan anda salah, coba lagi")

for i in range(20):
    if i % 2 == 0:
        continue
    print("angka ganjil" , i)   