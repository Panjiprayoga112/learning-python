# def sapa(nama, sapa = "halo"):
#     print(sapa, nama)

# sapa("alice")

# def profil_siapa(nama, umur, kota = "jakarta", pekerjaan = "belum bekerja"):
#     print(f"===PROFILE {nama.Uupper()}===")
#     print(f"umur = {umur} tahun")
#     print(f"kota = {kota}")
#     print(f"pekerjaan = {pekerjaan}")
#     print("=======")

# profil_siapa("eko",25)

nama_global = "alice"

def tampilkan_nama():
    print("nama:", nama_global)

tampilkan_nama()

def ubah_nama():

    global nama_global
    nama_global = "bob"
    print("nama lokal:", nama_global)

ubah_nama()
tampilkan_nama()