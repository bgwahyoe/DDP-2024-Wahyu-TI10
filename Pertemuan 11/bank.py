class Bank:
    # properti
    norek = ""
    nama = ""
    saldo = 0
    jmlNasabah = 0
    BANK = "Bank Syariah NF"

    # member2 konstruktor
    def __init__(self, no, nasabah, saldo):
        self.norek = no
        self.nama = nasabah
        self.saldo = saldo
        Bank.jmlNasabah += 1
    
    # member3 method
    def nabung(self, uang):
        self.saldo += uang

    def tarik(self, uang):
        self.saldo -= uang

    def cetak(self):
        print(Bank.BANK,
              "\n==========================",
              "\nNo. Rekening:", self.norek,
              "\nNama Nasabah:", self.nama,
              "\nsaldo: Rp. ", self.saldo,
              "\n=========================="
              )