print()
print("======Profil=====")
print()

#input
nama, nim, kelas, noTelp, alamat = "putri", "0110124247","SI08","085719218355","""Kp.Duren Baru Poncol Rt 03/05 No.18"""

#proses, output
print("Nama Mahasiswa",nama)
print("NIM", nim)
print("Kelas Mahasiswa: ", kelas)
print("Nomor Telepon Mahasiswa", noTelp)
print("Alamat Mahasiswa: ", alamat)

print()
print("======Program Mencari BB Ideal=====")
print()

#input
tb = int(input("Masukan Tinggi Badan: "))

#proses
bbIdeal = (tb - 100) - ((tb - 100) * 0.15)

#output
print("Berat Badan Ideal dengan tinggi badan", tb, "adalah", bbIdeal, "kg")
print(type(bbIdeal))

print()
print("NO. 4 ")
print()

#input
celcius = float(input("Masukan nilai celcius: "))

#proses
fahrenheit = (celcius*9/5)+32

#output
print(celcius, "derajat celcius sama dengan", fahrenheit, "derajat fahrenheit")

#input
#menentukan variabel apa saja yang ada didalam program

#proses
#apa yang akan dilakukan oleh program(kegiatan)

#output
#hasil dari proses (berupa apa)?

#input
# jari-jari, tinggi, phi, volumeTabungan, luasTabung, kelilingTabung
r = int(input("masukan jari-jari: "))
t = int(input("masukan tinggi: "))
phi = 3.14
#proses
volumeTabung = phi * r * r * t
luasTabung = 2 * phi * r * (r + t)
#output
print("volume tabung adalah", volumeTabung )
print ("luas tabung adalah", luasTabung)
