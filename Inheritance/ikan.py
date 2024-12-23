from animal import animal

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        super().__init__(nama, makanan, hidup, berkembang_biak)

    def info_ikan(self):
        super().info_animal()

ikan_koi = ikan("Koi", "Pelet", "Air", "Bertelur")
ikan_gurame = ikan("Gurame", "Pelet", "Air", "Bertelur")
print("====================================================")
ikan_gurame.info_ikan()