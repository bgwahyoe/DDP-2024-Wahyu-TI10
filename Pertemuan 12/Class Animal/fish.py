from animal import *

class Fish(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernafas, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernafas = bernafas
        self.habitat = habitat

    def info_fish(self):
        super().info_animal()
        print("Bernafas Menggunakan \t:", self.bernafas,
              "\nJenis Air \t\t:", self.habitat,
              "\n=====================")

# objek 1
hiu = Fish("Hiu", "Daging", "Air", "Melahirkan", "Insang", "Asin")
hiu.info_fish()

# objek 2
cupang = Fish("Cupang", "Pelet", "Air", "Bertelur", "Insang", "Asin")
cupang.info_fish()

# objek 3
paus = Fish("Paus", "Plankton", "Laut", "Melahirkan", "Paru - Paru", "Asin")
paus.info_fish()