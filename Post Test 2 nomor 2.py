print("========================================================================")

Handphone = input("Masukkan Nama Handphone : " )
RAM_Handphone = int(input("Masukkan RAM Handphone : "))
Memori_Handphone = int(input("Masukkan Memori Handphone : "))
Warna_Handphone = input ("Masukkan Warna Handphone : ")
Harga_Handphone = float(input("Masukkan Harga Handphone : "))

list = []

list.append(Handphone)
list.append(RAM_Handphone)
list.append(Memori_Handphone)
list.append(Warna_Handphone)
list.append(Harga_Handphone)

print("========================================================================")

print("Nama Handphone yang digunakan adalah",list[0])
print("Dengan RAM", list[1], "GB")
print("Dan Memori", list[2], "GB")
print("Warna Handphone yang dipakai berwarna", list[3])
print("Dengan Harga", list[4], "Rupiah")

print("========================================================================")

print("Variabel Handphone adalah :" , Handphone, "bertipe data :", type(Handphone), end="\n\n")
print("Variabel RAM Handphone adalah :" , RAM_Handphone, "bertipe data :", type(RAM_Handphone), end="\n\n")
print("Variabel Memori Handphone adalah :" , Memori_Handphone, "bertipe data :", type(Memori_Handphone), end="\n\n")
print("Variabel Warna Handphone adalah :" , Warna_Handphone, "bertipe data :", type(Warna_Handphone), end="\n\n")
print("Variabel Harga Handphone adalah :" , Harga_Handphone, "bertipe data :", type(Harga_Handphone), end="\n\n")

print("========================================================================")
