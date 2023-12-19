pwd_benar = 'nbl8'
pwd_benar2 = '8nbl'
pwd_benar3 = 'nblm15'

def cekpass(id_password, password, page):
    limit = 3
    i = 0
    while i < limit:
        pwd = input(f'Masukkan Password {id_password} untuk Halaman {page}= ')
        if pwd == password:  
            print(f'Password Benar, Selamat anda berhasil {page}')
            return True
        else:
            i += 1
            if i == limit:
                print('maaf kesempatan anda telah habis!')
                return False
            else:
                print(f'Password Salah. mohon dicoba lagi')

# Tes password pertama
tes1 = cekpass('pertama', 'nbl8', 1)
if tes1:
    # Tes password kedua
    tes2 = cekpass('kedua', '8nbl', 2)
    if tes2:
        # Tes password ketiga
        tes3 = cekpass('ketiga', 'nblm15', 3)
        if tes3:
            print('Selamat Anda Berhasil Login')
