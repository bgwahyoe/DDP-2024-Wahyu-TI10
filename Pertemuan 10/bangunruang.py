import math

# Luas Kubus 
def luas_kubus(sisi):
    luas = 6 * sisi * sisi
    print("Luas permukaan kubus adalah", luas)

# Luas Balok
def luas_balok(p, l, t):
    luas = 2 * (p * l + p * t + l * t)
    print("Luas permukaan balok adalah", luas)

# Luas Tabung
def luas_tabung(r, t):
    luas = 2 * math.pi * r * (r + t)
    print("Luas permukaan tabung adalah", luas)

# Luas Bola
def luas_bola(r):
    luas = 4 * math.pi * r * r
    print("Luas permukaan bola adalah", luas)

# Luas Kerucut
def luas_kerucut(r, s):
    luas = (math.pi * r ** 2) + (math.pi * r * s)
    print("Luas permukaan kerucut adalah",luas)
