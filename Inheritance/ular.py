from animal import animal

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        super().__init__(nama, makanan, hidup, berkembang_biak)

    def info_ular(self):
        super().info_animal()

ular_piton = ular("Piton", "Daging", "Rawa", "Bertelur")
anaconda = ular("Anaconda", "Daging", "Rawa", "Bertelur")
print("====================================================")
ular_piton.info_ular()