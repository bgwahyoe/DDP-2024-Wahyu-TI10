from dosen import *
from mahasiswa import *

# ciptakan objek
m1 = Mahasiswa("Budi", "Laki-laki", 22, "Teknik Informatika", 3)
m2 = Mahasiswa("Andini", "Perempuan", 21, "Sistem Informasi", 2)
d1 = Dosen("Sari", "Perempuan", 35, ".Spd, .M.T", "Dosen")
d2 = Dosen("Budi", "Laki-laki", 40, ".S.T, .M.T", "Dosen")


# gunakan fungsi
d1.setGaji(1000000)
d2.setGaji(2000000)

# cetak
m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()

