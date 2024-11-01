print("Status Anggota")
print("1. Gold")
print("2. Silver")
print("3. Bronze")


status = str(input("Masukkan Status Ke Anggotaan :")).lower()

if status == "gold" or status == "silver":  
  print("Selamat! Anda mendapatkan diskon :)")
else :
  print("Maaf, Anda belum mendapatkan diskon :(")
  