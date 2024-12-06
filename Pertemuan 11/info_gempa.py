from gempa import *

# objek
print("=============================================")
print("============ INFO GEMPA !!!!!  ===============")
print("=============================================")

gempa1 = Gempa("Banten", 1.2)
gempa1.dampak()

gempa2 = Gempa("Palu", 6.1)
gempa2.dampak()

gempa3 = Gempa("Cianjur", 5.6)
gempa3.dampak()

gempa4 = Gempa("Jayapura", 3.3)
gempa4.dampak()

gempa5 = Gempa("Garut", 4.0)
gempa5.dampak()

print("=============================================")