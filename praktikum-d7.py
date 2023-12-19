pwd_benar = 'si23d'
a = True
limit = 3
i = 0
while a:
    i += 1
    pwd = input('Masukkan Password')
    if pwd == pwd_benar:
       print('password benar! Selamat anda login')
    else:
        print('password salah')
        if i ==limit:
           print('kesempatan Anda Habis')
           a= False
        else:
           print(f'Kesempatan anda tersisa{limit-i}')
   
