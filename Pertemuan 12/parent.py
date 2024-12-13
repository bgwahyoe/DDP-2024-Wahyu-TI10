# Person class ( Orang Tua )
class Person :
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def berjalan(self):
        print(self.name, "sedang berjalan")
    
    def berbicara(self):
        if self.gender == "Laki-laki":
            print(self.name, "Tidak Bercerita karena dia", self.gender)
        else:
            print(self.name, "Bercerita karena dia", self.gender)

# Child class ( Anak )
class Supir(Person):
    def __init__(self, name, age, gender, sim):
        super().__init__(name, age, gender)
        self.sim = sim

    def mengendarai(self):
        print(self.name, "sedang mengendarai karena punya SIM", self.sim)
    
    # membuat def berjalan di anak
    def berjalan(self):
        super().berjalan()
        print("ini method supir")

# Child class ( Anak )
class Mahasiswa(Person):
    def __init__(self, name, age, gender, nim):
        super().__init__(name, age, gender)
        self.nim = nim
    
    def belajar(self):
        print(self.name, "sedang belajar")

# objek 1
budi = Person("Budi", 22, "Laki-laki")
budi.berbicara()    
# budi.mengendarai() # error karena method mengendarai hanya ada di class Supir
        
# objek 2
andini = Supir("Andini", 22, "Perempuan","A")
print(andini.sim)
andini.berbicara()
andini.mengendarai()
andini.berjalan()

# objek 3
sari = Mahasiswa("Sari", 22, "Perempuan", "123")
sari.belajar()
sari.berbicara()
sari.berjalan()