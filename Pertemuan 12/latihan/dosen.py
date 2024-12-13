from person import *

class Dosen(Person):
    gelar = ""
    jabatan = ""
    gaji = 0

    def __init__(self, nama, umur, gender, gelar, jabatan) :
        super().__init__(nama, umur, gender)
        self.gelar = gelar
        self.jabatan = jabatan
    
    def setGaji(self, uang):
        self.gaji += uang
    
    def cetak(self) :
        super().cetak()
        print("Gelar :", self.gelar,
              "\nJabatan :", self.jabatan,
              "\nGaji :", self.gaji,
              "\n=====================")