# Harga tetap masing-masing barang
harga_barang = {
    'minyak': 25000,
    'indomie': 5000,
    'beras': 75000,
    'gula': 25000,
    'kopi': 20000,
    'teh': 10000
}

# Meminta jumlah barang dari pengguna
jumlah_barang = {}
for barang in harga_barang:
    jumlah_barang[barang] = int(input(f"Masukkan jumlah {barang}: "))

# Menghitung total pembelian
total_pembelian = sum(harga_barang[barang] * jumlah_barang[barang] for barang in harga_barang)

# Menghitung total setelah diskon dan potongan diskon jika ada
if total_pembelian > 100000:
    potongan_diskon = total_pembelian * 0.1
    total_setelah_diskon = total_pembelian - potongan_diskon
else:
    potongan_diskon = 0
    total_setelah_diskon = total_pembelian

# Mencetak hasil
print(f"\nTotal harga: Rp {total_pembelian}")
if potongan_diskon > 0:
    print(f"Anda mendapatkan diskon 10%! Potongan diskon: Rp {potongan_diskon}")
    print(f"Total setelah diskon: Rp {total_setelah_diskon}")
else:
    print("Anda tidak mendapatkan diskon.")

# Mencetak total yang harus dibayar
print(f"Total yang harus dibayar: Rp {total_setelah_diskon:.2f}")
