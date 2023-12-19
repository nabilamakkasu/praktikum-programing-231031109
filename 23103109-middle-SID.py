'''
Misalkan anda diberikan tugas untuk membuat program struk pembelian pada kasir di perusahaan alat-alat komputer. Pilih 5 barang Alat Komputer dengan harga masing-masing barang kemudian buatkan program dan ouputnya seperti berikut.

- Buat list data perusahaan
mdata = [PT. XYZ Komputer,
        JL. BALAIKOTA NO.1,
        Kota Parepare,
        Nabila Makkasau,
        nabilamakkasau@gmail.com,
        Nabila
        15 agustus 2004]
(NOTED: ubah Nama Lengkap, e-mail, Nama Kasir, Tanggal-Bulan-Tahun Lahir)

- Buat Nested list untuk 5 barang:

djual = [['D0001','D0002','D0003','D0004','D0005'],
        ['pensil1','pulpen2','penggaris3','spidol4','penghapus5'],
        [2,5,7,8,3],
        [3,3,3,3,3]]
(NOTED: ubah nama barang dan harga barang sesuai keinginan)

- Hasil Runing
                                 PT. XYZ KOMPUTER
                          JL. BALAIKOTA NO.2 KOTA PAREPARE
                             e-Mail: mahasiswa@ith.ac.id


MANAJER           : Nama Lengkap
KASIR             : Nama Kasir
Tanggal Pembelian : 25 Oktober 2023
|--     16    --|--       19      --|--     15    --|--  8 --|--    14    --| 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
No. Kode Barang |    Nama Barang    |   H. Satuan   | Jumlah |     Total    |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1   D1101       | Barang1           |      Rp15000,-|    3   |     Rp45000,-|
2   D1102       | Barang2           |       Rp5000,-|    3   |     Rp15000,-|
3   D1103       | Barang3           |      Rp50000,-|    3   |    Rp150000,-|
4   D1104       | Barang4           |       Rp3000,-|    3   |     Rp15000,-|
5   D1105       | Barang5           |      Rp10000,-|    3   |     Rp30000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                    SUBTOTAL:           15   |    Rp245000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Summary:
Harga tertinggi adalah    : Rp50000,-  (D1103 - Barang3)
Harga terendah  adalah    : Rp3000,-   (D1104 - Barang4)
Harga rata-rata pembelian : Rp ,-
                                                   Parepare, 25 Oktober 2023
                                          



                                                         NAMA LENGKAP      
                                                         ------------
                                                            MANAJER

'''


# Write your code in below!

print('''
Nama\t\t: Nabila Makkasau
NIM\t\t:23103109
Nomor Komputer\t: Ganjil
Kelas\t\t: Sistem Informasi D''')

#Answer in below


# Buat list data perusahaan  
mdata = ['PT. XYZ Komputer',
        'JL. BALAIKOTA NO.1',
        'Kota Parepare',
        'Nabila Makkasau',
        'nabilamakkasau@gmail.com',
        'Nabila',
        '15 Agustus 2004']
djual =[['D0001','D0002','D0003','D0004','D0005'],
        ['pensil1','pulpen2','penggaris3','spidol4','penghapus5'],
        [2,5,7,8,3],
        [3,3,3,3,3]] 
r = 100

print(mdata[0].center(72))
print(f'{mdata[1]}{mdata[2]}'.center(72))
print(f'e-Mail = {mdata[4]}'.center(72))
print('\n')
print(f'''MANAJER              : {mdata[3]}
kasir                : {mdata[-2]}
tanggal pembelian    : {mdata[-1]}''')

print('- '*40)
print("|--             --|--               --|--           --|--    --|--           --|")
print('- '*40)
print("| No. Kode Barang |    Nama Barang    |   H. Satuan   | Jumlah |     Total     |")
print('- '*40)

print(f'1. {djual[0][0]}'.ljust(18)+'|'+f'{djual[1][0]}'.ljust(19)+'|'+f'Rp {djual[2][0]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp {3*djual[2][0]*r},-'.rjust(15)+'|')
print(f'1. {djual[0][1]}'.ljust(18)+'|'+f'{djual[1][1]}'.ljust(19)+'|'+f'Rp {djual[2][1]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp {3*djual[2][1]*r},-'.rjust(15)+'|')
print(f'1. {djual[0][2]}'.ljust(18)+'|'+f'{djual[1][2]}'.ljust(19)+'|'+f'Rp {djual[2][2]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp {3*djual[2][2]*r},-'.rjust(15)+'|')
print(f'1. {djual[0][3]}'.ljust(18)+'|'+f'{djual[1][3]}'.ljust(19)+'|'+f'Rp {djual[2][3]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp {3*djual[2][3]*r},-'.rjust(15)+'|')
print(f'1. {djual[0][4]}'.ljust(18)+'|'+f'{djual[1][4]}'.ljust(19)+'|'+f'Rp {djual[2][4]*r},-'.rjust(15)+'|'+'3'.center(8)+'|'+f'Rp {3*djual[2][4]*r},-'.rjust(15)+'|')
print('- '*40)
print('                                      SUBTOTAL:           15   |     Rp245000,-|')
print('- '*40)
print("Summary:")
print(f"Harga tertinggi adalah    : Rp{max(djual[2])*r:>6},-  ({djual[0][djual[2].index(max(djual[2]))]} - {djual[1][djual[2].index(max(djual[2]))]})")
print(f"Harga terendah  adalah    : Rp{min(djual[2])*r:>6},-  ({djual[0][djual[2].index(min(djual[2]))]} - {djual[1][djual[2].index(min(djual[2]))]})")
total_pembelian = sum(djual[2])*r
rata_rata_pembelian = total_pembelian / len(djual[2])*r
print(f"Harga rata-rata pembelian : Rp {rata_rata_pembelian},-\n")

print(f'                                                         {mdata[2][5:]},{mdata[6]}\n\n\n')
print(f"{mdata[3]:^140}")
print('\n')
print(f"{'MANAJER':^140}")


