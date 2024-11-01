# Membuat sebuah list
bilangan_bulat = [1, 2, 3, 4, 5] 
print(bilangan_bulat)

# Mengakses 1 elemen dalam list
print(bilangan_bulat[0])

# Mengubah 1 elemen dalam list
bilangan_bulat[0] = 10
print(bilangan_bulat)

# Menambahkan elemen di akhiran list dengan append()
bilangan_bulat.append(6)
print(bilangan_bulat)

# Menambahkan elemen dengan posisi tertentu dengan insert()
bilangan_bulat.insert(2,7)
print(bilangan_bulat)

#Menghapus elemen dengan remove()
bilangan_bulat.remove(7)
print(bilangan_bulat)

# Menghapus elemen dan menyimpan elemen yang dihapus dengan pop()
elemen_terhapus = bilangan_bulat.pop
print(bilangan_bulat)
print(elemen_terhapus)


my_list = [1,2,3,4,5]
my_list[3] = 6
print(my_list)

my_list.append(6)
my_list.remove(1)
my_list.insert(0,1)


print(my_list)

# Membuat Dictionary
kontak= { 1: '0997896','budi': '086754','ibu_budi':'086443'}
print(kontak)
print(type(kontak))
print(kontak['budi'])

kontak['cici'] =  '097887'
print(kontak)

#  Membuat match dan case
warna_lampu = input("Masukan warna lampu: ")

# cek apakah nilainya sesuai kondisi tertentu dan akan menjalankan program yang sesuai 
match warna_lampu:
    case "merah" | "MERAH" | "Merah" :
        print("Berhenti")
    case "kuning" | "KUNING" | "Kuning":
        print("Hati-hati")
    case "hijau" | "HIJAU" | "Hijau":
        print("Jalan")
    case _:
        print("Input tidak valid")

# Membuat tuple
bilangan_bulat = [1,2,3,4,5]
print(bilangan_bulat)

print(bilangan_bulat[0])

bilangan_bulat[0] = 30
print(bilangan_bulat)

# buatlah sebuah list yang berisi bilangan bulat kurang dari 10
bilangan_bulat = [1,2,3,4,5,6,7,8,9]
print(bilangan_bulat)

# sekaraang tambahkan elemen 'Hello' diakhir list
bilangan_bulat.append("hello")
print(bilangan_bulat)

## hapus elemen ke 3 dari list dan simpan elemennya
menghapus_elemen = bilangan_bulat.pop(2)
print(menghapus_elemen)
print(bilangan_bulat)
