from datetime import datetime, timedelta

# input waktu awal
waktu_awal = datetime.strptime('07:25','%H:%M')

# input penambahan waktu
penambahan_waktu = timedelta(hours=1,minutes=49)

# jumlahkan waktu
waktu_hasil = waktu_awal + penambahan_waktu

# format hasil dalam HH:MM
hasil_format = waktu_hasil.strftime('%H:%M')

# output hasil
print('outputnya:',hasil_format)


# tugas 2

from datetime import datetime, timedelta

# input waktu awal
waktu_awal = datetime.strptime('09:19','%H:%M')

# input waktu yang dikurangkan
waktu_kurang = timedelta(hours=1,minutes=35)

# hitung waktu sebelumnya 
waktu_hasil = waktu_awal - waktu_kurang

# format hasil dalam HH:MM
hasil_format = waktu_hasil.strftime('%H:%M')

# output hasil
print('outputnya:',hasil_format)


