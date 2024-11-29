#Program menentukan bilangan ganjil dan genap
print('##1. Program Bilangan Ganjil dan Genap ##')
print('=============')

# Input Bilangan
bilangan = int(input('masukan bilangan anda : '))

if bilangan % 2 == 0 :
    print(bilangan, 'Merupakan bilangan genap')
else:
    print(bilangan, 'Merupakan bilangan ganjil')

#Program menentukan nilai ujian
print('##2. Program menentukan nilai ujian ##')
print('=============')

# input nilai
nilai_ujian = int(input('Masukan Nilai anda : '))

# Proses dan Output
if nilai_ujian >= 75:
    print('Kamu dinyatakan Lulus')
else:
    print('Kamu dinyatakan Tidak Lulus')

#Program menentukan usia dan status
print('##3. Program menentukan usia dan status ##')
print('=============')

# Input usia
usia = int(input('Masukan Usia Anda : '))

if usia >= 18:
    print('Kamu Dewasa')
elif usia >= 13 and usia <=17:
    print('Kamu Remaja')
else:
    print('Kamu Anak-Anak')

#Program menentukan nilai keanggotaan 
print('##4. Program status keanggotaan ##')
print('=============')

# Input status 
status_anggota = input("""Daftar Keanggotaan Dibawah Ini
1. Gold
2. Silver
3. Bronzel
Masukan Pilihan Anda: """).lower()

# Proses dan Output
if status_anggota == 'gold' or status_anggota == 'silver' : 
    print('Selamat! anda mendapatkan diskon')
elif status_anggota == 'bronze' :
    print('Maaf anda tidak mendapatkan diskon')
else:
    print('Masukan kata dengan benar')

#Program menentukan pembelian diskon 
print('##5. Program pembelian diskon ##')
print('=============')

# Input
jumlah_pembelian = int(input('Masukan Jumlah Pembelian : '))
print(f"Anda Mendapatkan Diskon 10%") if jumlah_pembelian > 100 else print(" Anda Tidak Mendapat Diskon")
