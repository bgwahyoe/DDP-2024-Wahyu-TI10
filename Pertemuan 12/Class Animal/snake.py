from animal import *

class Snake(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, berbisa, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.berbisa = berbisa
        self.habitat = habitat

    def info_snake(self):
        super().info_animal()
        print("Berbisa \t\t:", self.berbisa,
              "\nHabitat \t\t:", self.habitat,
              "\n=====================")

# objek 1
kobra = Snake("Ular Kobra", "Hewan Kecil", "Darat", "Bertelur", "Ya", "Hutan Lembab")
kobra.info_snake()

# objek 2
piton = Snake("Ular Piton", "Hewan Kecil", "Darat", "Melahirkan", "Tidak", "Hutan Kering")
piton.info_snake()

# objek 3
daun = Snake("Ular Daun", "Hewan Kecil", "Darat", "Bertelur", "Tidak", "Hutan Rimba")
daun.info_snake()