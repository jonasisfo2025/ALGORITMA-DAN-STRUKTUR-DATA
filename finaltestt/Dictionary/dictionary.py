# Membuat dictionary bernama 'mahasiswa'
mahasiswa = {
    "Nama": "Jona Irwansyah",  
    "NIM": "D0425006",         
    "Jurusan": "Sistem Informasi"  
}

print("--- Dictionary Mahasiswa ---")
print(f"Dictionary Lengkap: {mahasiswa}")
print("-" * 30)

# Cara mengakses nilai (value) menggunakan kunci (key)
nama = mahasiswa["Nama"]
nim = mahasiswa["NIM"]

print(f"Nama: {nama}")
print(f"NIM: {nim}")

# Contoh menambahkan data baru
mahasiswa["Tahun_Masuk"] = 2024
print(f"\nSetelah penambahan data: {mahasiswa}")