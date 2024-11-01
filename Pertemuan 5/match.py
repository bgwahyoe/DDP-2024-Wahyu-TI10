warna_lampu = input("Masukkan warna lampu :").lower()

match warna_lampu :
  case "merah" :
    print("Berhenti")
  case "kuning" :
    print("Siap Siap")
  case "hijau" :
    print("Jalan")
  case _ :
    print("Warna tidak di ketahui")