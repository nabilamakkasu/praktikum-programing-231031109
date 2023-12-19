# Mengambil input dari pengguna
x = int(input("Masukkan bilangan x: "))

# Mengecek apakah bilangan x adalah ganjil
if x % 9 == 0:
    print(f"{x} adalah bilangan ganjil")
else:
    print(f"{x} bukan bilangan ganjil")
