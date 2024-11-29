kendaraan = ['beat karbo','motor', 200, 'pink', 3]
print(kendaraan)

kendaraan.append('10jt')
print(kendaraan)

kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'honda')
print(kendaraan)

angka_pilihan = int(input("""Masukan Pilihan:
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga
"""))

match angka_pilihan:
    case 1:
        print("Menghitung Luas Persegi")
        sisi = int(input("Masukan nilai sisi: "))
        luas_persegi = sisi ** 2
        print(f"Luas Persegi dengan sisi {sisi} cm, adalah {luas_persegi} cm^2")
    case 2:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = 3.14159 * (jari_jari ** 2)
        print(f"Luas lingkaran: {luas}")
    case 3:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print(f"Luas segitiga: {luas}")
    case _: 
        print("Input tidak valid")
    