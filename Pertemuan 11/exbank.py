from bank import *

# Objek
wahyu = Bank("001", "Wahyu", 10000000)
salman = Bank("002", "Salman", 50000000)
varrel = Bank("003", "Varrel", 20000000)


# Method
wahyu.nabung(5000000)
salman.tarik(2000000)
varrel.nabung(1000000)

# Cetak
print(Bank.BANK,
      "\n==========================")
wahyu.cetak(),
salman.cetak(),
varrel.cetak(),
print("Jumlah Nasabah: %i orang" %Bank.jmlNasabah)