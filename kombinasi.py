def combination(n, r):
    if r == 0 or r == n:
        return 1  
    return combination(n - 1, r - 1) + combination(n - 1, r)

n = int(input("Masukkan nilai n: "))
r = int(input("Masukkan nilai r: "))

if r > n:
    print("r tidak boleh lebih besar dari n!")
else:
    print(f"Kombinasi C({n}, {r}) adalah {combination(n, r)}")
