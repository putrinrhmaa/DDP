from animal import animal

class burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna_bulu):
        super().__init__(nama, makanan, hidup, berkembang_biak), 
        self.paruh = paruh 
        self.warna_bulu = warna_bulu

    def info_burung(self):
        super().info_animal(),
        print("Paruh \t\t\t : ", self.paruh,
              "\nWarna Bulu \t\t : ", self.warna_bulu)
        
burung_beo = burung("Beo", "Jagung", "Darat", "Bertelur", "Melengkung", "Warna-warni")
burung_merpati = burung("Merpati", "Padi", "Darat", "Bertelur", "Lurus","Putih")
print("====================================================")
burung_merpati.info_burung()