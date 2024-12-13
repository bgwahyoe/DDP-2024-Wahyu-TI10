class Animal :
    # konstruktor
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    # method informasi
    def info_animal(self):
        print("\n=== Informasi Hewan ===",
              "\nNama Hewan \t\t:", self.nama,
              "\nMakanan \t\t:", self.makanan,
              "\nHidup di \t\t:", self.hidup,
              "\nBerkembang Biak \t:", self.berkembang_biak)   
        
             
# objek 1
kucing = Animal("Kucing", "Ikan", "Darat", "Melahirkan")
kucing.info_animal()

# objek 2
anjing = Animal("Anjing", "Daging", "Darat", "Melahirkan")
anjing.info_animal()

# objek 3
gurame = Animal("Gurame", "Pelet", "Air", "Bertelur")
gurame.info_animal()