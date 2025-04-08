# Perulangan (loop)

# for kondisi: JIKA KONDISI TERPENUHI \
# aksi JALANKAN AKSI 

angkan_list = [0, 2, 4, 8, 10] # ini adalah list
print(angkan_list)
      
# angka = (0)
# print(angka)
# angka += 1 # angka = angka 1
# print(angka)
# angka += 1
# print(angka) 

# for-loop
for i in angkan_list:
    print(f"i sekarang  -> {i}")

print('loop berakhir \n')

# dengan range
for i in  range(5):
    print(f"i sekarang  -> {i}")

print('loop renge berakhir \n')

for i in range(1,10):
    print(f"i sekarang  -> {i}")

print('loop renge berakhir \n')

# for bintang
for i in range(1,4):
    print("*"  * i)

print('loop renge berakhir \n')   

# Membuat pola bintang seperti di papan tulis menggunakan range
for i in range(1, 4):  # Loop akan berjalan 3 kali (untuk baris 1, 2, dan 3)
    jumlah_bintang = 2 * i - 1
    print("*" * jumlah_bintang)