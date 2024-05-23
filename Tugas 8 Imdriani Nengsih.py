print("  Nama  : Imdriani Nengsih")
print("  No BP : 2310431035")
print("  Shift : 4")
print()
print("         ======= Menu Data Keuangan =======")
print("1. Simpan Data")
print("2. Hapus Data")
print("3. Tampilkan Data")
print("4. Keluar")

while True:
    print()
    n = int(input("Pilih menu : "))
    print()

    data = {}
    with open("keuangan.txt", "r") as file:
        for line in file:
            date, alasan, nominal, tipe = line.strip().split(',')
            data[date] = {"keterangan": alasan, "jumlah": nominal, "tipe": tipe}

    def simpan(data):
        with open("keuangan.txt", 'w') as file:
            for key, value in data.items():
                file.write(f"{key},{value['keterangan']},{value['jumlah']},{value['tipe']}\n")

    if (n == 1):
        date = input("tanggal tansaksi(DD-MM-YYYY) : ")
        alasan = input("Keterangan transaksi : ")
        nominal = input("Jumlah transaksi(Rp.) : ")
        tipe = input("Pemasukan/pengeluaran : ")
        data[date] = {"keterangan": alasan, "jumlah": nominal, "tipe": tipe}
        simpan(data)
        print("Transaksi telah ditambahkan")

    elif (n == 2):
        date = input("Tanggal transaksi yang akan dihapus (DD-MM-YYYY) : ")
        if date in data:
            del data[date]
            simpan(data)
            print("Transaksi sudah dihapus")
        else:
            print("Transaksi tidak ditemukan")

    elif (n == 3):
        print("{:<15} {:<30} {:<15} {:<15}".format("tanggal", "keterangan", "jumlah", "Tipe"))
        print("-" * 75)
        for date, info in data.items():
            print("{:<15} {:<30} {:<15} {:<15}".format(date, info["keterangan"], info["jumlah"], info["tipe"]))

    elif (n == 4):
        print("Terimakasih dan sampai jumpa lagi")
        break
    else :
        print("Menu tidak tersedia")