#Membuat list
umur1 = [2001, 2002, 2003, 2004, 2005]
print("Membuat list:", umur1)

#mengakses list
print ("Menampilkan element 3: ", umur1[2])
print ("Mengambil element ke 2 sampai 4: ", umur1[1:4])
print ("Mengambil element terakhir: ", umur1[4])

#mengubah element ke 4 dengan nilai lain
umur1[3] = 2006

print ("Mengubah element ke 4 dengan niai lain:", umur1)

#mengubah element ke 4 sampai element terakhir
umur1[3:] = 2006,2007

print ("Mengubah element ke 4 sampai element terakhir:", umur1)

#mengambil 2 bagian dari list pertama dan jadikan list kedua

umur1 = [2004, 2005]
print("Mengambil 2 bagian dari list pertama:", umur1)

#membuat list 2

umur2 = [2004, 2005]
print("Membuat list kedua :", umur2)

#menambah list kedua dengan 3 nilai

umur2 = [2004, 2005, 2006, 2007, 2008]
print("Menambah list kedua dengan 3 nilai:", umur2)

#Menggabungkan list pertama dengan list kedua

umur1umur2 = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008]
print("Menggabungkan list 1 dan list 2 :", umur1umur2)
