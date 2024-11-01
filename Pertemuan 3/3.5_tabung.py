#Menghitung Luas dan Keliling Tabung
# Input dari pengguna
r = float(input("Masukkan jari-jari alas tabung (cm): "))
t = float(input("Masukkan tinggi tabung (cm): "))

# Menghitung luas permukaan dan keliling alas, dibulatkan ke integer
luas = int(2 * 22/7 * r * (r + t))  # Luas permukaan tabung
keliling = int(2 * 22/7 * r)        # Keliling lingkaran alas

# Mencetak hasil
print("Luas Permukaan Tabung:", luas, "cm²")
print("Keliling Alas Tabung:", keliling, "cm")
