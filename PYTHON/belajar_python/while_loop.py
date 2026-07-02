password_benar = "12345"
max_percobaan = 3
percobaan = 0

while percobaan < max_percobaan:
    password_input = input("Masukkan password: ")
    if password_input == password_benar:
        print("Password benar! Akses diberikan.")
        break
    else:
        percobaan += 1
        print(f"Password salah! Percobaan ke-{percobaan}.")

else:
    print("Anda telah mencapai batas percobaan. Akses ditolak.")
    