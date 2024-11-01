list = [1,2,3,4] #list
list.append(5) #menambahkan elemen pada list
list.insert(0,8) #menambahkan angka 8 setelah indeks 0
list.remove(1) #menghapus beedasarkan indeks
poplist = list.pop(3) #mengambil elemen dr indeks 3
# print(list[1])
print(list)
print(poplist)

#tuple
my_tuple = (1,2,3,4)
print(my_tuple[1])

# my_tuple[3] = 2
# print(my_tuple)

#dictionary

dictionary = {
  'nama' : 'Wahyu',
  'nim' : 24047, #int gabisa 0
  'Rombel' : 'TI10'
}

print(dictionary["nama"])
print(dictionary["Rombel"])
print(type('nama'))
print(type(dictionary['nim']))


