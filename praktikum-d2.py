print('praktikum-2 \n\n')
print('=======ini and=======')
a = True
b = False
hasil = a and a 
print('Nilai',a,'and',a,'adalah',hasil)
hasil = a and b 
print('Nilai',a,'and',b,'adalah',hasil)
hasil = b and a 
print('Nilai',b,'and',a,'adalah',hasil)
hasil = b and a 
print('Nilai',b,'and',a,'adalah',hasil)
hasil = b and b
print('Nilai',b,'and',b,'adalah',hasil)
print('\n=======ini or=======')
hasil = a and a 
print('Nilai',a,'and',a,'adalah',hasil)
hasil = a and b 
print('Nilai',a,'and',b,'adalah',hasil)
hasil = b and a 
print('Nilai',b,'and',a,'adalah',hasil)
hasil = b and a 
print('Nilai',b,'and',a,'adalah',hasil)
hasil = b and b
print('Nilai',b,'and',b,'adalah',hasil)

print('\n=======ini not=======')
hasil = not a
print('Hasil not',a,'adalah',hasil)
hasil = not b
print('Hasil not',b,'adalah',hasil)

print('\n=======ini xor=======')
hasil = a ^ a 
print('Nilai',a,'xor',a,'adalah',hasil)
hasil = a ^ b 
print('Nilai',a,'xor',b,'adalah',hasil)
hasil = b ^ a 
print('Nilai',b,'xor',a,'adalah',hasil)
hasil = b ^ b
print('Nilai',b,'xor',b,'adalah',hasil)



print('=======ini nand=======')
a = True
b = False
hasil = not(a and a) 
print('Nilai',a,'nand',a,'adalah',hasil)
hasil = not(a and b) 
print('Nilai',a,'nand',b,'adalah',hasil)
hasil = not(b and a) 
print('Nilai',b,'nand',a,'adalah',hasil)
hasil = not(b and b)
print('Nilai',b,'nand',b,'adalah',hasil)

print('=======ini nor=======')
hasil = not(a and a) 
print('Nilai',a,'nor',a,'adalah',hasil)
hasil = not(a and b) 
print('Nilai',a,'nor',b,'adalah',hasil)
hasil = not(b and a) 
print('Nilai',b,'nor',a,'adalah',hasil)
hasil = not(b and b)
print('Nilai',b,'nor',b,'adalah',hasil)


print('\n=======ini nxor=======')
hasil = a ^ a 
print('Nilai',a,'nxor',a,'adalah',not hasil)
hasil = a ^ b 
print('Nilai',a,'nxor',b,'adalah',not hasil)
hasil = b ^ a 
print('Nilai',b,'nxor',a,'adalah',not hasil)
hasil = b ^ b
print('Nilai',b,'nxor',b,'adalah',not hasil)

print('=================IS')
a = 5
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)
a = 6
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

print('=================IS NOT')
a = 5
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)
a = 6
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)

print('\n================= in')
nama = 'Bacharuddin Jusuf Habibie'
test = 'rud'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'bach'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('\n================= not in')
nama = 'Nabila Makkasau'

test = 'rud'
cek = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'bach'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'ib'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

est = 'a'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'u'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'e'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek)) 

test = 'o'
cek  = test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('\n================= in')
data = ['Institut'
        'Teknologi',
        'Bacharuddin',
        'Jusuf'
        'Habibie']
test1 =  'habibie'      
test2 = 'Parepare'
test3 = 'Kampus'
test4 = 'Institut'

cek = test1 in data
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 in data
print(test2,'terdapat di data adalah '+str(cek))
cek = test3 in data
print(test3,'terdapat di data adalah '+str(cek))
cek = test4 in data
print(test4,'terdapat di data adalah '+str(cek))

print('\n================= not in')
#TUGAS dengan cara yang sama buat operator utuk not in
data = ['Nabila Makkasau']
print('data adalah',data)
test1 = 'nabila'
test2 = 'Makkasau'

cek = test1 in data
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 in data
print(test2,'terdapat di data adalah '+str(cek))
        
#INI OPERATOR BITWISE
a = 15
b = 8
b+= 2004
print('\n================= AND')
print('Nilai',a,'dalam biner      =',format(a,'08b'))
print('Nilai',b,'dalam biner      =',format(b,'08b'))
print('-----------------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))

print('\n================= not in')
a = 15
b = 8
b+= 2004
print('\n================ QR')        
print('Nilai',a,'dalam biner      =',format(a,'08b'))
print('Nilai',b,'dalam biner      =',format(b,'08b'))
print('-----------------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))

print('\n============Ini xor============')
hasil = a ^ b
print('nilai',a,'xor',b,'adalah',not hasil)
hasil = a ^ a
print('nilai',a,'xor',a,'adalah',not hasil)
hasil = b ^ a
print('nilai',b,'xor',a,'adalah',not hasil)
hasil = b ^ b
print('nilai',b,'xor',b,'adalah',not hasil)

print('\n============Ini not============')
hasil = c or c
print('hasil not',a,'adalah',hasil)
hasil = not a
print('hasil not',b,'adalah',hasil) 

print('\n============Ini not============')
hasil = b or b
print('hasil not',a,'adalah',hasil)
hasil = not a
print('hasil not',b,'adalah',hasil)

print('\n============geser kanan============')
a = 16
c = a >> 2
print(c) # output : 4

print('\n============geser kiri============')
a = 16
c = a << 2
print(c) # output : 4

print('============not and============')
hasil = a & b
print('Nilai',a,'&',b,'adalah',hasil)
hasil = b & a
print('Nilai',b,'&',a,'adalah',hasil)
hasil = b & b
print('Nilai',b,'&',b,'adalah',hasil)
hasil = b & a
print('Nilai',b,'&',a,'adalah',hasil)

print('============not or============')
hasil = a | b
print('nilai',a,'|',b,'adalah',hasil)
hasil = b | a
print('nilai',b,'|',a,'adalah',hasil)

print('\n============not xor============')
hasil = a ^ b
print('nilai',a,'xor',b,'adalah',not hasil)
hasil = a ^ a
print('nilai',a,'xor',a,'adalah',not hasil)
hasil = b ^ a
print('nilai',b,'xor',a,'adalah',not hasil)
hasil = b ^ b
print('nilai',b,'xor',b,'adalah',not hasil)

print('\n============not geser kanan============')
a = 16   # reprensi binar dari 16 adalah '10000'
c = ~(a >> 2)
print(c)

print('\n============not geser kiri============')
a = 16   # reprensi binar dari 16 adalah '10000'
c = ~(a<<2)
print(c)









        
