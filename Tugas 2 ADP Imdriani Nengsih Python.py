print("Nama    : Imdriani Nengsih")
print("NIM     : 2310432035")
print("Shift   : 4")
print("")
print("")
print("=========================== LAYANAN PEMESANAN TIKET PESAWAT ===========================")
print("Selamat Datang di Layanan Pemesanan Tiket Pesawat")
print("Silakan Masukkan Data Diri Anda")
print("")
nama=str(input("             Nama          : "))
umur=str(input("             Umur          : "))
jenis_kelamin=str(input("             Jenis Kelamin : "))
print("")
print("")
print("")
print("")
print("_-_-_-_-_-_-_-_-_-_-_-_-_- TUJUAN KEBERANGKATAN DARI PADANG _-_-_-_-_-_-_-_-_-_-_-_-_-")
print("")
print("Silakan Pilih Tujuan Pernerbangan Anda")
print("")
print("                               |   1. MAKASAR   |")
print("                               |   2. BANTEN    |")
print("                               |   3. BALI      |")
print("---------------------------------------------------------------------------------------")
penerbangan=int(input("Masukkan nomor urut tujuan penerbangan anda : "))
if (penerbangan==1):
    print("    Rute penerbangan anda : PADANG-MAKASAR")
if(penerbangan==2):
    print("    Rute penerbangan anda : PADANG-BANTEN")
if (penerbangan==3):
    print("    Rute penerbangan anda : PADANG-BALI")
print("")
print("")
print("")
print("")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_- KELAS PENERBANGAN _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("             _______________________________________________________")
print("            |     Kelas Penerbangan     ||           Harga          |")
print("            |=======================================================|")
print("            |   1. EKONOMI              ||       Rp.1.000000        |")
print("            |   2. BISNIS               ||       Rp.3.000000        |")
print("            |   3. FIRST CLASS          ||       Rp.7.000000        |")
print("             -------------------------------------------------------")
print(" Diskos 25% untuk pembelian lebih dari 3 tiket")
print("-----------------------------------------------------------------------------------------")
maskapai=int(input("Silakan masukan jenis maskapai anda : "))
jumlah_kursi=int(input("Jumlah kursi yang akan dipesan      : "))
if (maskapai==1):
    total_harga= harga_tiket= jumlah_kursi*1000000
    total_harga= harga_tiket1= 0.75*jumlah_kursi*1000000
    if(jumlah_kursi<=3):
        print("Total harga                         : Rp.",harga_tiket)
    if(jumlah_kursi>3):
        print("Total harga                         : Rp.",harga_tiket1)
if (maskapai==2):
    total_harga=harga_tiket2=jumlah_kursi*3000000
    total_harga=harga_tiket3=0.75*jumlah_kursi*3000000
    if(jumlah_kursi<=3):
        print("Total harga                         : Rp.",harga_tiket2)
    if (jumlah_kursi>3):
        print("Total harga                         : Rp.",harga_tiket3)
if (maskapai==3):
    total_harga=harga_tiket4=jumlah_kursi*7000000
    total_harga=harga_tiket5=0.75*jumlah_kursi*7000000
    if(jumlah_kursi<=3):
        print("Total harga                         : Rp.",harga_tiket4)
    if(jumlah_kursi>3):
        print("Total harga                         : Rp.",harga_tiket5)
print("")
print("")
print("")
print("")
print("                              STRUK PEMESANAN")
print("                    Nama           :",nama)
print("                    Umur           :",umur)
print("                    Jenis Kelamin  :",jenis_kelamin)
print("                    --------------------------------")
if (penerbangan==1):
    print("                    Kota Tujuan    : MAKASAR")
if (penerbangan==2):
    print("                    Kota Tujuan    : BANTEN")
if(penerbangan==3):
    print("                    Kota Tujuan    : BALI")
if (maskapai==1):
    print("                    Jenis Maskapai : EKONOMI")
if(maskapai==2):
    print("                    Jenis Maskapai : BISNIS")
if(maskapai==3):
    print("                    Jenis Maskapai : FIRST CLASS")
print("                    Jumlah Tiket   : ",jumlah_kursi)
if (maskapai==1):
    total_harga= harga_tiket= jumlah_kursi*1000000
    total_harga= harga_tiket1= 0.75*jumlah_kursi*1000000
    if(jumlah_kursi<=3):
        print("                    Total Harga    : Rp.",harga_tiket)
    if(jumlah_kursi>3):
        print("                    Total Harga    : Rp.",harga_tiket1)
if (maskapai==2):
    total_harga=harga_tiket2=jumlah_kursi*3000000
    total_harga=harga_tiket3=0.75*jumlah_kursi*3000000
    if(jumlah_kursi<=3):
        print("                    Total Harga    : Rp.",harga_tiket2)
    if (jumlah_kursi>3):
        print("                    Total Harga    : Rp.",harga_tiket3)
if (maskapai==3):
    total_harga=harga_tiket4=jumlah_kursi*7000000
    total_harga=harga_tiket5=0.75*jumlah_kursi*7000000
    if(jumlah_kursi<=3):
        print("                    Total Harga    : Rp.",harga_tiket4)
    if(jumlah_kursi>3):
        print("                    Total Harga    : Rp.",harga_tiket5)
print("")