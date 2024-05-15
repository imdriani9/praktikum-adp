print("          Nama  : Imdriani Nengsih")
print("          No.BP : 2310431035")
print("          Shift : 4")
print("          Modul : VII (fungsi)")
print()
print()

n = int(input("Masukkan banyak percobaan : "))

p = []
for i in range (n) :
   entri = i + 1
   p.append(entri)

v0 = []
for i in range (n) :
    print("Masukkan kecepatan awal benda (m/s) ke-",i+1,":")
    entri = float(input())
    v0.append(entri)

a = []
for i in range (n) :
    print("Masukkan percepatan benda (m/s^2) ke-",i+1,":")
    entri = float(input())
    a.append(entri)

t = []
for i in range (n) :
    print("Masukkan waktu tempuh benda (s) ke-",i+1,":")
    entri = float(input())
    t.append(entri)

kecepatan_akhir =[]
for i in range (n) :
    def v1(v0, a, t):
     v1 = v0 + a*t
     return v1
    f = v1(v0[i], a[i], t[i])
    entri = f
    kecepatan_akhir.append(f)

jarak =[]
for i in range (n) :
  def s(v0, t, a):
    s = v0*t + (1/2)*a*t**2
    return s
  g = s(v0[i], t[i], a[i])
  entri = g
  jarak.append(entri)

print()
print()
print("   n   |   Kecepatan Awal(m/s)   |   Percepatan(m/s^2)   |   Waktu(s)   |   Kecepatan Akhir(m/s)   |   Jarak(m)   ")
print("------------------------------------------------------------------------------------------------------------------")
for i in range (n) :
  print(f"   {p[i]}   |           {v0[i]}           |          {a[i]}          |      {t[i]}     |           {kecepatan_akhir[i]}            |       {jarak[i]}")
  print("------------------------------------------------------------------------------------------------------------------")
print()
print()