print("       Nama     : Imdriani Nengsih")
print("       N0. BP   : 2310431035")
print("       Shift    : 4")
print("       Modul    : VI")
print()
print()

print("                       Daftar Barang, Harga dan Stok Toko Kelontong Pak Budi")
print()
barang = ["Gula  ", "Telur ", "Beras ", "Teh   ", "Kopi  ", "Sayur ", "Minyak", "Tepung"]
harga_stok =[[20000, 30000, 15000, 30000, 25000, 15000, 20000, 20000 ],
             [20, 12, 25, 5, 3, 20, 17, 5]]

print("                            Barang   |   Harga (Rp.)    |   Stok(Kg)   ")
print("                            ---------------------------------------")
for i in range(0,8) :
         print(f"                            {barang[i]}   |       {harga_stok[0][i]}      |     {harga_stok[1][i]}     ")
print()
print()
print()
print()
untung = []
for i in range (0,8) :
    entri = harga_stok[0][i]*harga_stok[1][i]
    untung.append(entri)

for i in range (0,8) :
   for j in range(0,7) :
        if (untung[j] > untung[j+1]) :
            k = untung[j]
            untung[j] = untung[j+1]
            untung[j+1] = k
            l = barang[j]
            barang[j] = barang[j+1]
            barang[j+1] = l
print("Keuntungan Toko Kelontong Pak Budi")
print()
print("     barang    |  Keuntungan(Rp.)  ")
print("--------------------------------")
for i in range(0,8) :
    print(f"     {barang[i]}    |     {untung[i]}     ")
jumlah = sum(untung)
print("--------------------------------")
print("    jumlah     : Rp.",jumlah,"    ")
print()
print()
print("a. Nama barang dengan keuntungan terbesar adalah",barang[7],"dengan keuntungan Rp.",untung[7])
print("b. Nama barang dengan keuntungan terkecil adalah",barang[0],"dengan keuntungan Rp.",untung[0])
print("c. Total keuntungan toko kelontong milik Pak Budi sebesar Rp.",jumlah)
print()