class Orang:
        #variabel (properti)
        def __init__(self, nama, usia, gender, alamat):
            self. nama = nama
            self. usia = usia
            self.gender = gender
            self.alamat = alamat

        #fungsi (method)
        def ngomong (self):
                print("Saya bisa berbicara karena saya", self.gender)
        def jalan(self, kata):
                print("Saya bisa berjalan", kata)

        # objek1
        supir = Orang()
        supir.nama = "agus"
        print(supir.nama)
        supir.jalan("Kapan?")
        supir.sim = "A"
        print(supir.sim)

        # objek2
        mahasiswa = Orang()
        print(mahasiswa.nama)
