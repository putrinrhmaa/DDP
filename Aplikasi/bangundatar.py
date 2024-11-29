import math 


# Deklarasi Fungsi
def l_persegi(sisi):
    hitung = sisi * sisi
    print(f'Luas Persegi Adalah {hitung}')

def l_persegi_panjang(p, l):
    hitung = p * l
    print(f'Luas Persegi Panjang Adalah {hitung}')

def l_segitiga(alas, tinggi):
    hitung = 1/2 * alas * tinggi
    print(f'Luas Segitiga Adalah {hitung}')

def l_lingkaran(r):
    hitung = r * 3.14 * r 
    print(f'Luas Lingkaran Adalah {hitung}')

def l_jajargenjang(alas, tinggi):
    hitung = alas * tinggi
    print(f'Luas Jajargenjang Adalah {hitung}')
