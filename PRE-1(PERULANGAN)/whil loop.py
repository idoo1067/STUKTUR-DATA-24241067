tinggi = 3

for i in range(tinggi):
    spasi = ' ' * (tinggi - i - 1)
    bintang = '*' * (2 * i + 1)
    print(spasi + bintang)

