class Gempa:
    lokasi = ''
    skala = ''

    # Contraction
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    # Method/fungsi
    def dampak(self):
        if self.skala <2 :
            ket = 'Gempa tidak berasa'
        elif self.skala >2 and self.skala <4 :
            ket = 'Bangunan Rtak-Retak'
        elif self.skala >4 and self.skala <6 :
            ket = 'Bangunan Roboh'
        else : 
            ket = 'Bangunan roboh berpotensi tsunami'

        print('Lokasi Gempa', self.lokasi, '\nSkala Gempa', self.skala, '\nDampak Gempa', ket)