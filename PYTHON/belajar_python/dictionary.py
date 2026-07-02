siswa = {
    "nama": "panji",
    "umur": 23,
    "kelas": "12A"
}
print(siswa)

for key in siswa:
    print(key, ":", siswa[key])

for key, value in siswa.items():
    print(key, ":", value)

siswa["nama"] = "budi"
print(siswa)


