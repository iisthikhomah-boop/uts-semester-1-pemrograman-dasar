# Soal 1
def balik_kalimat(kalimat):
    """Membalik urutan karakter dalam sebuah kalimat."""
    
    return kalimat[::-1]

kalimat_input = input("1. Masukkan kalimat:HALLO ")
hasil_balik = balik_kalimat(kalimat_input)
print(f"   Tampilan terbalik: OLLAH {hasil_balik}")
print("-" * 30)


# Soal 2
def hitung_karakter(kalimat, karakter):
    """Menghitung jumlah karakter tertentu dalam sebuah kalimat."""
   
    jumlah_1 = kalimat.count(karakter)
    
    
    return jumlah_1

kalimat_input = input("2. Masukkan kalimat:AKUTAKUT ")
karakter_input = input("   Masukkan huruf yang ingin dihitung:A ")


if len(karakter_input) > 1:
    karakter_input = karakter_input[0]
    print(f"   Menggunakan karakter pertama '{karakter_input}' saja.")

jumlah_karakter = hitung_karakter(kalimat_input, karakter_input)
print(f"   Jumlah huruf '{karakter_input}' dalam kalimat: {jumlah_karakter}")
print("-" * 30)

# SOAL 3
def hitung_jumlah_karakter():
    
    kalimat_input = input("AKU GAK SUKA PEMROGRAMAN: ")

    jumlah_karakter = len(kalimat_input)
    
    # 3. Menampilkan hasil
    print("\n--- Hasil Perhitungan ---")
    print(f"Kalimat yang dimasukkan: A '{kalimat_input}'")
    print(f"Jumlah total karakter (termasuk spasi): 24 ")

hitung_jumlah_karakter()

# Soal 4
print("4. Buat Tampilan angka berikut: 122333444455555666666...")
print("   Tampilan: 122333444455555666666")

# Soal 5
print("5. Buat Tampilan angka berikut: 6666665555544443333221...")
print("   Tampilan: 6666665555544443333221")

# Soal 6
print("6. Buat Tampilan angka berikut: 112123123412345123456...")
print(" 112123123412345123456  Tampilan: ")

# Soal 7
print("7. Buat Tampilan angka berikut: 654321543214321321211...")
print("   Tampilan: 654321543214321321211")

# Soal 8
print("8. Buat Tampilan angka berikut: 112333123455555123456 ...")
print("   Tampilan: 112333123455555123456")

# Soal 9
print("9. Buat Tampilan angka berikut:  12212344441234566666...")
print("   Tampilan:  12212344441234566666 ")

# Soal 10
print("10. Buat Tampilan angka berikut: 654321555554321333211...")
print("    Tampilan: 654321555554321333211" )

# Soal 11
print("11. Buat Tampilan angka berikut: 666666123454444123221...")
print("    Tampilan: 666666123454444123221 ")

# Soal 12
print("12. Buat Tampilan angka berikut: 122123123455555666666123456712345678999999999 ...")
print("    Tampilan:  122123123455555666666123456712345678999999999")

# Soal 13
print("13. Buat Tampilan angka berikut: 112333444412345123456777777788888888123456789..")
print("    Tampilan: 112333444412345123456777777788888888123456789")

# Soal 14
print("14. Buat Tampilan angka berikut: 8888888887777777654321543214444333211...")
print("    Tampilan: 8888888887777777654321543214444333211 ")

# Soal 15
print("15. Buat Tampilan angka berikut: 876543217654321666666555554321321221...")
print("    Tampilan: 876543217654321666666555554321321221")

# Inisialisasi variabel string untuk menampung hasil output
soal16 = ""
soal17 = ""
soal18 = ""
soal19 = ""
soal20 = ""
soal21 = ""
soal22 = ""
soal23 = ""
soal24 = ""
soal25 = ""
soal26 = ""
soal27 = ""
soal28 = ""
soal29 = ""
soal30 = ""

# SOAL NOMOR 16
# Pola: n+4, n-2, ... 
# Deret: 1, 5, 3, 7, 5, 9, 7, 11, 9, 13, 11, 15
print("## Soal 16: Pola n+4, n-2")
n = 1
terms = 12 
for i in range(terms):
    soal16 += str(n) + " "
    if i % 2 == 0:  
        n += 4      
    else:           
        n -= 2    
print("Deret:", soal16)
print("-" * 30)

# SOAL NOMOR 17
# Pola: n+10, n-5, ... 
# Deret: 2, 12, 7, 17, 12, 22, 17, 27, 22, 32
print("## Soal 17: Pola n+10, n-5")
n = 2
terms = 10
for i in range(terms):
    soal17 += str(n) + " "
    if i % 2 == 0:  
        n += 10     
    else:          
        n -= 5      
print("Deret:", soal17)
print("-" * 30)

# SOAL NOMOR 18
# Pola: n-3, n+5, ... 
# Deret: 5, 2, 7, 4, 9, 6, 11, 8, 13, 10, 15, 12
print("## Soal 18: Pola n-3, n+5")
n = 5
terms = 12 
for i in range(terms):
    soal18 += str(n) + " "
    if i % 2 == 0: 
        n -= 3      
    else:         
        n += 5     
print("Deret:", soal18)
print("-" * 30)

# SOAL NOMOR 19
# Pola: n*3, n-5, ...
# Deret: 3, 9, 4, 12, 7, 21, 16, 48, 43, 129
print("## Soal 19: Pola n*3, n-5")
n = 3
terms = 10 
for i in range(terms):
    soal19 += str(n) + " "
    if i % 2 == 0:  
        n *= 3      
    else:         
        n -= 5     
print("Deret:", soal19)
print("-" * 30)

# SOAL NOMOR 20
# Pola: n+1, n+2, n+3, ... 
# Deret: 1, 2, 4, 7, 8, 10, 13, 14, 16, 19, 20, 22, 25
print("## Soal 20: Pola n+1, n+2, n+3 (Siklus)")
n = 1
increments = [1, 2, 3]
for o in range(13):
    soal20 += str(n) + " "
    step = increments[o % 3]
    n += step
print("soal nomor 20 :"+soal20)

# SOAL 21
n = 1
for d in range(10):
    soal21 += str(n) + " "
    n *= 2
print("soal nomor 21 :"+soal21)

# SOAL 22
n = 3
faktorial = 1
soal22 = str(n) + '! = '
for q in range(n, 0, -1):
    soal22 += str(q) + " "
    if q > 1:
        soal22 += "x "
    faktorial *= q
soal22 += "= " + str(faktorial)
print("soal nomor 22 :"+soal22)

# SOAL 23
maks = 45
a, b = 0, 1
soal23 += str(a) + "," + str(b) + ","
while True:
    c = a + b
    if c > maks:
        break
    soal23 += str(c) + ","
    a, b = b, c
print("soal nomor 23 :"+soal23)

# SOAL 24
n_awal = 3
n_akhir = 30
for u in range(n_awal, n_akhir + 1):
    if u % 3 == 0:
        soal24 += str(u) + " "
print("soal nomor 24 :"+soal24)

# SOAL 25
n_awal = 4
n_akhir = 30
for u in range(n_awal, n_akhir + 1):
    if u % 4 == 0:
        soal25 += str(u) + " "
print("soal nomor 25 :"+soal25)

# SOAL 26
n_awal = 1
n_akhir = 10
jumlah_bulat_positif = 0
for i in range(n_awal, n_akhir + 1):
    if i > 0:
        jumlah_bulat_positif += 1
        soal26 += str(i) + " "
print("soal nomor 26 :"+soal26)
print("total bilangan bulat positif dari", n_awal, n_akhir)

# SOAL 27
n_awal = 1
n_akhir = 20
total_genap = 0
for i in range(n_awal, n_akhir + 1):
    if i % 2 == 0:
        total_genap += 1
        soal27 += str(i) + " "
print("soal nomor 27 :"+soal27)
print("total bilangan ganjil dari", n_awal, "hingga", n_akhir, "adalah", total_genap)

# SOAL 28
n_awal = 10
n_akhir = 50
jumlah_ganjil = 0
for i in range(n_awal, n_akhir + 1):
    if i % 2 != 0:
        jumlah_ganjil += 1
        soal28 += str(i) + " "
print("soal nomor 28 :"+soal28)
print("total bilangan ganjil dari", n_awal, "hingga", n_akhir, "adalah", jumlah_ganjil)

# SOAL 29
n_awal = 10
n_akhir = 30
prima_list = []
for n in range(n_awal, n_akhir, +1):
    if n > 1:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                break
        else:
            prima_list.append(n)
print("soal nomor 29 : bilangan primanya adalah =", end=" ")
for p in prima_list:
    print(f"{p}", end=" : ")
print()

# SOAL 30
n_awal = 10
n_akhir = 30
prima_list = []
for j in range(n_awal, n_akhir, +1):
    if j > 1:
        for i in range(2, int(j**0.5)+1):
            if j % i == 0:
                break
        else:
            prima_list.append(j)
print("soal nomor 30 :", "".join(str(p) for p in prima_list))
print("jumlah total bilangan :", len(prima_list))