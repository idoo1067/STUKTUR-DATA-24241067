# Variabel global untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menambahkan mahasiswa
def create():
    nama = input("Masukkan nama mahasiswa: ")
    data_mahasiswa.append(nama)
    print(f"Mahasiswa '{nama}' berhasil ditambahkan.\n")

# Fungsi untuk menampilkan daftar mahasiswa
def read():
    if len(data_mahasiswa) == 0:
        print("Belum ada data mahasiswa.\n")
    else:
        print("Daftar Mahasiswa:")
        for i, nama in enumerate(data_mahasiswa):
            print(f"{i}. {nama}")
        print()  # Baris kosong setelah daftar

# Fungsi untuk mengubah nama mahasiswa
def update():
    read()
    index = input("Masukkan indeks mahasiswa yang ingin diubah: ")
    if index.isdigit():
        index = int(index)
        if 0 <= index < len(data_mahasiswa):
            nama_baru = input("Masukkan nama baru: ")
            nama_lama = data_mahasiswa[index]
            data_mahasiswa[index] = nama_baru
            print(f"Nama mahasiswa '{nama_lama}' telah diubah menjadi '{nama_baru}'.\n")
        else:
            print("Indeks tidak ditemukan.\n")
    else:
        print("Input harus berupa angka.\n")

# Fungsi untuk menghapus mahasiswa
def delete():
    read()
    index = input("Masukkan indeks mahasiswa yang ingin dihapus: ")
    if index.isdigit():
        index = int(index)
        if 0 <= index < len(data_mahasiswa):
            nama = data_mahasiswa.pop(index)
            print(f"Mahasiswa '{nama}' berhasil dihapus.\n")
        else:
            print("Indeks tidak ditemukan.\n")
    else:
        print("Input harus berupa angka.\n")

# Fungsi utama
def main():
    while True:
        print("=== Menu Manajemen Mahasiswa ===")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Daftar Mahasiswa")
        print("3. Ubah Nama Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            create()
        elif pilihan == "2":
            read()
        elif pilihan == "3":
            update()
        elif pilihan == "4":
            delete()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Menjalankan program
if __name__ == "__main__":
    main()
