print("        Nama  : Imdriani Nengsih")
print("        NIM   : 2310431035")
print("        Shift : 4")
print()
n = int(input("Masukkan banyak elemen A : "))
a = []
for i in range(n):
    elem = int(input("Masukkan elemen ke-"+str (i+1) +" : "))
    if 0 < elem > 9:
        print("Elemen yang dimasukkan harus bilangan dari 0 sampai 9.")
        print("Silahkan masukkan elemen kembali.")
        i-=1
    else:
        a.append(elem)
print()
k = int(input("Masukkan banyak elemen B : "))
b = []
for j in range(k):
    elem = int(input("Masukkan elemen ke-" + str(j + 1) + " = "))
    if elem < 0 or elem > 9:
        print("Elemen yang dimasukkan harus bilangan dari 0 sampai 9.")
        print("Silahkan masukkan elemen kembali.")
        j -= 1
    else:
        b.append(elem)
print()
print("Elemen yang hanya ada di A : ", end=" ")
for i in range(n):
    found = False
    for j in range(k):
        if a[i] == b[j]:
            found = True
            break
    if not found:
        print(a[i], end=" ")
print()
print("Elemen yang hanya ada di B : ", end=" ")
for i in range(k):
    found = False
    for j in range(n):
        if b[i] == a[j]:
            found = True
            break
    if not found:
        print(b[i], end=" ")
print()
print("Elemen yang ada di A dan di B : ", end=" ")
for i in range(n):
    for j in range(k):
        if a[i] == b[j]:
            print(a[i], end=" ")
            break
print()
print("note : Jika Kosong, maka tidak ada elemennya")