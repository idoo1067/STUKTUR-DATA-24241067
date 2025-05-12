# Meminta jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# Dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

# Menginput data untuk setiap mahasiswa
for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa ke-{i+1}:")
    nim = input("  Masukkan NIM: ")
    nama = input("  Masukkan Nama: ")
    
    jumlah_mk = int(input("  Masukkan jumlah mata kuliah: "))
    nilai_mk = []

    for j in range(jumlah_mk):
        mk = input(f"    Nama mata kuliah ke-{j+1}: ")
        nilai = float(input(f"    Nilai untuk {mk}: "))
        nilai_mk.append((mk, nilai))
    
    data_mahasiswa[nim] = {
        "nama": nama,
        "nilai_mk": nilai_mk
    }

# Menampilkan rata-rata dan semua data mahasiswa
print("\nData Mahasiswa dan Nilai Rata-rata:")
for nim, info in data_mahasiswa.items():
    nama = info["nama"]
    nilai_mk = info["nilai_mk"]
    rata_rata = sum([nilai for _, nilai in nilai_mk]) / len(nilai_mk)
    
    print(f"\nNIM: {nim}")
    print(f"Nama: {nama}")
    print("Mata Kuliah dan Nilai:")
    for mk, nilai in nilai_mk:
        print(f"  - {mk}: {nilai}")
    print(f"Rata-rata Nilai: {rata_rata:.2f}")
