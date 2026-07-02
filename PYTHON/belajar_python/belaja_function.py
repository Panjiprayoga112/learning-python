print("====DATA SISWA====")

file = open("nilai siswa.txt", "w")

while True:
    nama = input("masukkan nama(enter untuk selesai): ")
    if nama == "":
     break

    nilai = input("masukkan nilai:")

    file.write(nama + "=" + nilai + "\n")
    print("data",nilai,"berhasil disimpan")

file.close()
print("program selesai")



    
