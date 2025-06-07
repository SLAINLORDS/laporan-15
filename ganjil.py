def sum(n):
    if n == 1:
        return 1  
    return n + sum(n - 2) 

# Contoh penggunaan
n = int(input("Masukkan bilangan ganjil terbesar dalam deret: "))
if n % 2 == 0:
    print("Harap masukkan bilangan ganjil!")
else:
    print(f"Jumlah deret ganjil hingga {n} adalah {sum(n)}")