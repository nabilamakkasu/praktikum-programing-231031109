print('praktikum-d4')
print()
print('Nama Lengkap : Nabila Makkasau')
print('NIM          : 23103109')
print('Prodi        : Sistem Informasi')
print()
angkatan = 2023
print('Angkatan adalah', angkatan)
print()
email        = 'nabilamakkasau@gmail.com'


a = [2,3,1,0,3,1,0,9,7]
# akses item
print(a)
print('item indeks-0',a[0])       # tanpa format
print(f'item indeks-0 {a[0]}')    # dengan format
print(f'item indeks-3 {a[3]}') 
print(f'item indeks-terakhir {a[len(a)-1]}') 
# akses item indeks negatif
print(f'item indeks:-1 {a[-1]}') 
print(f'item indeks:terakhir (-1) {a[-len(a)]}')
print(f'item indeks:pertama (-9) {a[-len(a)]}')
print(f'item indeks:1 (-8) {a[-len(a)]}')
print(f'item indeks:5 (4) {a[-len(a)]}')
# akses indeks batas
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:1,2,... {a[1:]}')
print(f'item indeks:3,4,... {a[3:]}')
print(f'item indeks:0,1,2,... {a[:3]}')
print(f'item indeks:0,1,2,3,4,... {a[:5]}')
print(f'item indeks:semua {a[:]}')
# pengirisan indeks
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:2,3,4 {a[2:5]}')
print(f'item indeks:[1:8] {a[1:-1]}')
# nested list
kelas = [('pemrograman',3),
         ('pancasila',3),
         ('sains',2)
         ]
print(f'data kelas {kelas}')
kelas.append(('agama',3))
print(f'data kelas {kelas}')
kelas.append(('kalkulus',3))
print(f'data kelas {kelas}')

#Nama Mata Kuliah 1: pemrograman dengan jumlah sks:3
print('Nama Mata Kuliah 1:',kelas [0][0],'dengan jumlah sks :',kelas [0][1])
#Nama Mata Kuliah 2: pancasila dengan jumlah sks:2
print('Nama Mata Kuliah 2:',kelas [1][0],'dengan jumlah sks :',kelas [1][1])
#Nama Mata Kuliah 3: sains dengan jumlah sks:3
print('Nama Mata Kuliah 3:',kelas [2][0],'dengan jumlah sks :',kelas [2][1])
#Nama Mata Kuliah 4: agama dengan jumlah sks:2
print('Nama Mata Kuliah 4:',kelas [3][0],'dengan jumlah sks :',kelas [3][1])
# Nama Mata Kuliah 5: kalkulus dengan jumlah sks:3
print('Nama Mata Kuliah 5:',kelas [4][0],'dengan jumlah sks :',kelas [4][1])

data = [('Nabila Makkasau',2023,'Aktif'),
        (90,89,93,97,99),
        (20,22),
        ('S1-Reguler','Sistem Informasi D','Ganjil')]

#Nama Mahasiswa: Nabila Makkasau
print('Nama Mahasiswa :',data [0][0])
#Nim Mahasiswa: 23103109
print('NIM Mahasiswa :',a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8])
#Program pendidikan Nabila Makkasau: Sistem Informasi D S1-Reguler
print('Program Pendidikan',data [0][0],'adalah :',data [3][1],data[3][0])
#Angkatan : 2023-Ganjil
print('Angkatan :',data [0][1],'-',data[3][2])
#Jumlah nilai nabila Makkasau adalah: 5
print('Jumlah nilai',data [0][0],'adalah :',len(data[1]))
#Data terkecil Nabila Makkasau adalah: 89
print('Data terkecil',data [0][0],'adalah :',min(data[1]))
#Data terbesar Nabila Makkasau adalah: 99
print('Data terbesar',data [0][0],'adalah :',max(data[1]))
#Rata-rata Nabila Makkasau adalah: 92.25
rata = sum(data[1])/len(data[1])
print('Rata-rata nilai',data [0][0],'adalah :',rata)



