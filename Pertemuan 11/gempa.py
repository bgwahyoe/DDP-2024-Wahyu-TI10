class Gempa:
    #konstruktor inialisasi atribut
    def __init__(self, lokasi, skala): # method = fungsi di dalam kelas
        self.lokasi = lokasi
        self.skala = skala
    
    # method
    def dampak(self):
        if self.skala <= 2:
            dampak = "Gempa tidak berasa"
        elif self.skala >= 2 and self.skala <= 4:
            dampak = "Gempa bangunan retak retak"
        elif self.skala >= 4 and self.skala <= 6:
            dampak = "Gempa bangunan roboh"
        elif self.skala > 6:
            dampak = "Gempa bangunan hancur dan berpotensi tsunami"

        #print
        print("Gempa di", self.lokasi, "dengan skala :", self.skala, "Dampaknya :", dampak)