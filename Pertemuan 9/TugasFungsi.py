print()
print("## Nomor 1 ##")

def celcius_ke_fahrenheit(celcius):
    fahrenhit = (celcius * 9/5) + 32
    return fahrenhit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

print()
print("## Nomor 2 ##")
def ganjil_genap(bilangan):
    boolean = bilangan % 2 == 0
    return boolean

print(ganjil_genap(4))
print(ganjil_genap(7))

print()
print("## Nomor 3 ##")
def nilai(keterangan):
    if keterangan >= 80:
        print("Lulus :)")
    elif keterangan < 80:
        print("Gagal :(")
    else:
        print("Tidak diketahui")

nilai(80)
nilai(60)

print()
print("## Nomor 4 ##")
def bilangan_ganjil(bilangan):
    return[i for i in range(bilangan) if i % 2 == 1]

print(bilangan_ganjil(20))

