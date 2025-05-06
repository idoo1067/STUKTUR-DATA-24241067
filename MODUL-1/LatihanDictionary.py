def input_data_mahasiswa():
    data_mahasiswa = {}

    while True:
        print("\nMasukkan data mahasiswa:")
        nim = input("NIM      : ").strip()
        if nim in data_mahasiswa:
            print("NIM sudah ada, silakan masukkan NIM yang berbeda.")
            continue
        nama = input("Nama     : ").strip()
        jurusan = input("Jurusan  : ").strip()

        data_mahasiswa[nim] = {
            'nama': nama,
            'jurusan': jurusan
        }

        lanjut = input("Tambah data lagi? (y/n): ").strip().lower()
        if lanjut != 'y':
            break

    return data_mahasiswa


def cari_mahasiswa(data, nim):
    return data.get(nim, None)


def tampilkan_data(data):
    if not data:
        print("Data mahasiswa kosong.")
        return

    print("\nData Mahasiswa:")
    print(f"{'NIM':<15}{'Nama':<25}{'Jurusan':<20}")
    print("-" * 60)
    for nim, info in data.items():
        print(f"{nim:<15}{info['nama']:<25}{info['jurusan']:<20}")


def main():
    data_mahasiswa = input_data_mahasiswa()

    while True:
        print("\nMenu:")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan NIM")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == '1':
            tampilkan_data(data_mahasiswa)
        elif pilihan == '2':
            nim = input("Masukkan NIM yang dicari: ").strip()
            hasil = cari_mahasiswa(data_mahasiswa, nim)
            if hasil:
                print(f"\nData ditemukan:\nNama    : {hasil['nama']}\nJurusan : {hasil['jurusan']}")
            else:
                print("Data tidak ditemukan.")
        elif pilihan == '3':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
